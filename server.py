"""
Executing this function initiates the application of emotion
detection to be executed over the Flask channel and deployed on
localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Flask route that receives text from a web request and returns an emotion analysis.

    This function extracts the 'textToAnalyze' parameter from the URL query string,
    processes it using the emotion_detector function, and returns a formatted
    string response for display in the web interface.

    Returns:
        str: A formatted string containing scores for all emotions and the
             dominant emotion, or an error message if the input is invalid.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    if response.get('dominant_emotion') is None:
        return 'Invalid text! Please try again!'

    return (
            f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
            f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )

@app.route("/")
def render_index_page():
    """
    Serves the main application page.

    This function handles the root URL ('/') and renders the initial
    HTML template for the web interface.

    Returns:
        Rendered template: The content of the 'index.html' file.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
