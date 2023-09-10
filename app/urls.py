from django.urls import path
from app.views import write,voice, title,description,speech
urlpatterns = [
    path('write/',write,name = "write"),
    path("speech/", speech, name="speech"),
    path('voice/', voice, name="voice"),
    path('title',title, name= "title"),
    path('description/', description, name = "description")
]
