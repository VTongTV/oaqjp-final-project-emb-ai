"""Module for emotion detection web server."""
from typing import Optional

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector


app = Flask("EmotionDetector")


@app.route("/")
def render_index_page() -> str:
    """Render and return the index page template.

    Returns:
        str: Rendered HTML for the index page.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route() -> str:
    """Handle emotion detection requests from the query parameter.

    The route expects a query parameter named ``textToAnalyze``. When the
    underlying emotion detector determines the input is invalid (blank or
    otherwise), a user-friendly error message is returned.

    Returns:
        str: A formatted string with emotion scores and dominant emotion, or
        an error message when the input is invalid.
    """
    text_to_analyze: Optional[str] = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    # Format the response string using parentheses to satisfy linters
    result_str = (
        "For the given statement, the system response is "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, "
        f"'fear': {fear_score}, 'joy': {joy_score}, "
        f"'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    )
    return result_str


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)