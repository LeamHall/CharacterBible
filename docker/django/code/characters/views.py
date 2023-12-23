# from django.shortcuts import render
from django.views.generic import ListView

from .models import Character


class CharacterListView(ListView):
    model = Character
    context_object_name = "character_list"
    template_name = "character_list.html"


class CharacterDetailView(ListView):
    model = Character
    template_name = "character_detail.html"
