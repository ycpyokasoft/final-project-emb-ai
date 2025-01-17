import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Submit the JSON object and headers to the API and receive the response
    response = requests.post(url, json=myobj, headers=header)

    emotion_dict = dict()

    if response.status_code == 400:
        emotion_dict['anger'] = None
        emotion_dict['disgust'] = None
        emotion_dict['fear'] = None
        emotion_dict['joy'] = None
        emotion_dict['sadness'] = None
        emotion_dict['dominant_emotion'] = None
        return emotion_dict

    # Extract the set of emotions
    output = json.loads(response.text)
    
    emotion_dict['anger'] = float(output['emotionPredictions'][0]['emotion']['anger'])
    emotion_dict['disgust'] = float(output['emotionPredictions'][0]['emotion']['disgust'])
    emotion_dict['fear'] = float(output['emotionPredictions'][0]['emotion']['fear'])
    emotion_dict['joy'] = float(output['emotionPredictions'][0]['emotion']['joy'])
    emotion_dict['sadness'] = float(output['emotionPredictions'][0]['emotion']['sadness'])

    dominant_emotion = ""
    max_score = -100
    for emotion_key in emotion_dict.keys():
        if emotion_dict[emotion_key] > max_score:
            max_score = emotion_dict[emotion_key]
            dominant_emotion = emotion_key
    
    emotion_dict['dominant_emotion'] = dominant_emotion
    # return the text response
    return emotion_dict