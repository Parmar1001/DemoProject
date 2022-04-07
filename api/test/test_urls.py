from api.views import *
from django.test import SimpleTestCase
from django.urls import resolve, reverse


class TestUrls(SimpleTestCase):

    def test_Branch_api_resolve(self):
        url = reverse('Branch')
        print(resolve(url))
        self.assertEquals(resolve(url).func, BranchViewSet)


    def test_Customer_api_resolve(self):
        url = reverse('Customer')
        print(resolve(url))
        self.assertEquals(resolve(url).func, CustomerViewSet)
        

    def test_Notification_api_resolve(self):
        url = reverse('Notification')
        print(resolve(url))
        self.assertEquals(resolve(url).func, NotificationViewSet)


    def test_Contact_api_resolve(self):
        url = reverse('Contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, ContactViewSet)
