# characters/urls.py

from django.urls import path

from .views import CharacterListView, CharacterDetailView

urlpatterns = [
    path("<uuid:pk>/", CharacterDetailView.as_view(), name="character_detail"),
    path("", CharacterListView.as_view(), name="character_list"),
]
