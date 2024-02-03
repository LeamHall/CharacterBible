# apis/urls.py

from django.urls import path

from .views import CharacterAPIView

urlpatterns = [
    path("", CharacterAPIView.as_view(), name = "character_list"),
]
