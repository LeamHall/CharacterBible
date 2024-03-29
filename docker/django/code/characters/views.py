# from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Character


class CharacterListView(ListView):
    model = Character
    context_object_name = "character_list"
    template_name = "character_list.html"


class CharacterDetailView(DetailView):
    model = Character
    context_object_name = "character"
    template_name = "character_detail.html"
