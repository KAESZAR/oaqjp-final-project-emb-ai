import requests
import json

def emotion_detector(text_to_analyse):
    # Verificar si la entrada está en blanco
    if not text_to_analyse.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }, 400
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobject = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=myobject, headers=header)
    
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        emotion_scores = response_dict['emotionPredictions'][0]['emotion']
        
        # Extrae las emociones requeridas
        emotions = {key: emotion_scores[key] for key in ['anger', 'disgust', 'fear', 'joy', 'sadness']}
        
        # Encuentra la emoción dominante
        dominant_emotion = max(emotions, key=emotions.get)
        
        result = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }

        return result, 200
    else:
        raise Exception("Error in API call: " + response.text)
