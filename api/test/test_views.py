import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

class TestBrachCreateApi(APITestCase):
    
    def test_branch(self):
        factory = APIRequestFactory()
        request = factory.post('Branch', {'branch_name': 'Api Testing', 'branch_city':'Testing Api Views', 'branch_state':'api state'}, format='json')