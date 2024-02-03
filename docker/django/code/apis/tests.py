# apis/test.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from characters.models import Character

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.character = Character.objects.create(
            first_name = "Alba",
            last_name = "Lefron",
            notes = "Al",
        )

    def test_api_listview(self):
        response = self.client.get(reverse("character_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Character.objects.count(), 1)
        self.assertContains(response, "Alba Lefron")

