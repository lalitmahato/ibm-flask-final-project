"""Emotion Detector Package"""
import json
import requests

DOMAIN = "https://sn-watson-emotion.labs.skills.network"
URL = f'{DOMAIN}/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADER = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
TIMEOUT = 100

def get_dominant_emotion(emotion):
    """Return the dominant emotion"""
    highest_score = 0
    highest_label = None
    for k,v in emotion.items():
        if v > highest_score:
            highest_score = v
            highest_label = k
    return highest_label


def emotion_detector(text_to_analyze):
    """Analyze the emotion of text"""
    # Create the payload with the text to be analyzed
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Make a POST request to the API with the payload and headers
    response = requests.post(URL, json=myobj, headers=HEADER, timeout=TIMEOUT)
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        emotion_predictions = formatted_response.get('emotionPredictions')
        emotion = emotion_predictions[0].get('emotion') if emotion_predictions else {}
        emotion["dominant_emotion"] = get_dominant_emotion(emotion)
    else:
        emotion = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    return emotion
