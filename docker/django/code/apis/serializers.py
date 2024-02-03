#apis/serializers.py

from rest_framework import serializers

from characters.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("id", "first_name", "last_name", "notes", "name")

