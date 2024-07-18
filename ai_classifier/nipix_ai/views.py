from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import tensorflow as tf

# 1. String input will be provided 
@api_view(["POST"])
def sentiment_analyser(request):
    # get the data from the frontend
    data = request.data
    print(data["sentence"])

    # perform sentimental analysis
    # 1. loading the model
    model_1 = tf.keras.models.load_model('E://aiml-intern/ai_word_classifier/server/ai_classifier/nipix_ai/models/gru_model')
    print("The Models have been loaded")

    # 2. predicting the request data
    y_pred = model_1.predict([data["sentence"]])
    y_pred = tf.squeeze(tf.argmax(y_pred, axis = 1))

    # 4. convert it to readable
    if y_pred == 0:
        y_pred = "positive"
    elif y_pred == 1:
        y_pred = "negative"
    elif y_pred == 2:
        y_pred = "neutral"
    elif y_pred == 3:
        y_pred = "irrelevant"
    else: 
        y_pred = "unknown"

    # returning some response to the users
    context = {
        "message" : "App is working Perfectly",
        "data": data,
        "output": y_pred
    }
    return Response(context)