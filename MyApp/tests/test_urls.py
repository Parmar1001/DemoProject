from django.test import SimpleTestCase
from django.urls import reverse, resolve
from MyApp.views import *


class TestUrls(SimpleTestCase):

    def test_home_resolve(self):
        url = reverse('Home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home_view)


    def test_profile_resolve(self):
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ProfileView)


    def test_customer_info_resolve(self):
        url = reverse('customer_info', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, CustomerInfo)


    def test_transfer_money_resolve(self):
        url = reverse('transfer')
        print(resolve(url))
        self.assertEquals(resolve(url).func, TransferView)


    def test_request_money_resolve(self):
        url = reverse('requestmoney')
        print(resolve(url))
        self.assertEquals(resolve(url).func, RequestMoneyView)


    def test_notification_resolve(self):
        url = reverse('notification')
        print(resolve(url))
        self.assertEquals(resolve(url).func, NotificationView)


    def test_service_resolve(self):
        url = reverse('service')
        print(resolve(url))
        self.assertEquals(resolve(url).func, ServiceView)


    def test_clients_resolve(self):
        url = reverse('clients')
        print(resolve(url))
        self.assertEquals(resolve(url).func, ClientsView)


    def test_contact_resolve(self):
        url = reverse('contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, contactView)


# 13 test casess are hear