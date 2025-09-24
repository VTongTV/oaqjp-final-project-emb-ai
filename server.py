"""Module for emotion detection web server."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector


app = Flask("EmotionDetector")


@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')


@app.route("/emotionDetector")
def emotion_detector_route():
    """Handle emotion detection requests."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Format the response string
    result_str = f"For the given statement, the system response is " \
                 f"'anger': {anger_score}, 'disgust': {disgust_score}, " \
                 f"'fear': {fear_score}, 'joy': {joy_score}, " \
                 f"'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    return result_str


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)