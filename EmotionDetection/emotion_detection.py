#Import request, json
import requests  
import json

#function to get response and analyze

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' #url of watson lab
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = myobj, headers = header) #get response
    formatted_response = json.loads(response.text)#convert to json

    anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"] #get anger score
    disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"] #get disgust score
    fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"] #get fear score
    joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"] #get joy score
    sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"] #get sadness score

    dominant_emotion_score = max(anger_score,disgust_score,fear_score,joy_score,sadness_score) #get the maximum emotion score
    mydict = {"anger": anger_score, "disgust": disgust_score, "fear": fear_score, "joy": joy_score, "sadness": sadness_score} # create dictionary
    
    #get the dominent emotion from dictionary having max score
    for emotion,score in mydict.items():
        global dominant_emotion
        if score == dominant_emotion_score:
            dominant_emotion = emotion

    mydict["dominant emotion"] = dominant_emotion #update doctionary with dominant emotion 

    return mydict