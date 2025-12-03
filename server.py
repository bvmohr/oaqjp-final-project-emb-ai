"""
server.py - deploys the interface for the flask application, Emotion Detector
"""
# import required libraries
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    emo_detector - function to analyze text for its emotional scores regarding anger, fear, 
    disgust, sadness, and joy. The function returns these values, along with the dominant 
    emotion, in a formatted string.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    anger_score = response['anger']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    disgust_score = response['disgust']
    dominant_emotion = response['dominant_emotion']

    # error handling part b
    if dominant_emotion is None:
        result = "Invalid text! Please try again!"
    else:
        result = f"For the given statement, the system response is \'anger\': {anger_score}, \
        \'disgust\': {disgust_score}, \'fear\': {fear_score}, \'joy\': {joy_score}, \'sadness\': {sadness_score}. \
        The dominant emotion is <b>{dominant_emotion}</b>"
    return result

@app.route("/")
def render_index_page():
    """
    Renders the provided index.html file to show user interface. 
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
