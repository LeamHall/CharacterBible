from rest_framework import generics

from characters.models import Character
from .serializers import CharacterSerializer

class CharacterAPIView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

