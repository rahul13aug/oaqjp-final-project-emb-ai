from flask import Flask, render_template, request #import Flask, render template and request
from EmotionDetection.emotion_detection import emotion_detector #import function

app = Flask("Emotion Detector")

@app.route('/emotionDetector')

def emo_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant emotion']}. "

@app.route("/")

def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5000)



