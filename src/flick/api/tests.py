import json
import random
import string

from django.test import TestCase
from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework.test import APIClient


class FlickTestCase(TestCase):
    AUTHENTICATE_URL = reverse("authenticate")
    NAME = "Alanna Zhou"

    def get_random_str(self):
        letters = string.digits
        random_string = "".join(random.choice(letters) for i in range(5))
        return random_string

    def setUp(self):
        self.client = APIClient()

    def _create_user_and_login(
        self,
        username="",
        name=NAME,
        social_id="",
        social_id_token="",
        social_id_token_type="facebook",
    ):
        """Returns the auth token."""
        random_str = self.get_random_str()
        data = {
            "username": username,
            "name": name,
            "profile_pic": "",
            "social_id": social_id or random_str,
            "social_id_token": social_id_token or random_str,
            "social_id_token_type": social_id_token_type,
        }
        response = self.client.post(self.AUTHENTICATE_URL, data)
        self.assertEqual(response.status_code, 200)
        token = json.loads(response.content)["data"]["auth_token"]
        return token


class FlickTransactionTestCase(TransactionTestCase):
    AUTHENTICATE_URL = reverse("authenticate")
    NAME = "Alanna Zhou"

    def get_random_str(self):
        letters = string.digits
        random_string = "".join(random.choice(letters) for i in range(5))
        return random_string

    def setUp(self):
        self.client = APIClient()

    def _create_user_and_login(
        self,
        username="",
        name=NAME,
        social_id="",
        social_id_token="",
        social_id_token_type="facebook",
    ):
        """Returns the auth token."""
        random_str = self.get_random_str()
        data = {
            "username": username,
            "name": name,
            "profile_pic": "",
            "social_id": social_id or random_str,
            "social_id_token": social_id_token or random_str,
            "social_id_token_type": social_id_token_type,
        }
        response = self.client.post(self.AUTHENTICATE_URL, data)
        self.assertEqual(response.status_code, 200)
        token = json.loads(response.content)["data"]["auth_token"]
        return token
