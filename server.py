''' Server program to implement sentiment analysis of text '''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def index():
    ''' Display index on root '''
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    ''' Emotion detection route '''
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return_text = f"For the given statement, the system response is 'anger': {response['anger']}, "
    return_text += f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
    return_text += f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
    return_text += f"The domination emotion is <b>{response['dominant_emotion']}</b>."

    return return_text

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
