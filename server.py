'''Emotion Detector'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze Emotion of the text"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response.get('dominant_emotion', None)
    if dominant_emotion:
        msg = "For the given statement, the system response is"
        for k,v in response.items():
            if k != "dominant_emotion":
                msg = f"{msg} '{k}': {v}"
        dominant_emotion_msg =  f". The dominant emotion is {dominant_emotion}."
        message = msg + dominant_emotion_msg
    else:
        message = "Invalid text! Please try again!."
    return message

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
