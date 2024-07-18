from django.urls import path
from nipix_ai import views

urlpatterns = [
    path('home', views.sentiment_analyser),
]
