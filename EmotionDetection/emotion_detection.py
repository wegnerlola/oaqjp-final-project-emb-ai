import requests
import json

def emotion_detector(text_to_analyse: str) -> dict:
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        emotions = response_dict['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        result = dict(emotions) # Creates a copy of the scores
        result['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
        result = {
            'anger': None, 
            'disgust': None, 
            'fear': None,
            'sadness': None,
            'joy': None,
            'dominant_emotion': None
        }
    return result
