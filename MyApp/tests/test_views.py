from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse


class TestViews(TestCase):


    def test_home_page(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)  


    def test_clients_page(self):
        response = self.client.get('/clients/')
        self.assertEquals(response.status_code, 200)    


    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200) 


    def test_service_page(self):
        response = self.client.get('/service/')
        self.assertEquals(response.status_code, 200)    


    def test_contact_page(self, full_name='Test01', email='test01@gmail.com', message='Test going good ', date=''):
        contact_cerate_url = reverse('contact')
        response = self.client.post(contact_cerate_url,{full_name:full_name, email:email, message:message, date:date}) 
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'MyApp/contact.html')


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_profile_post(self, profile_pic='media/MyApp/sta/about.jpeg' ,phonenum='chetan' ,balance='3000' ,account_type='Current' ,state='Madhya Pradesh', city='Indore', branch_name='SBI' ):
        # client = Client()
        self.client.login(username='chetan', password='demo')
        profile_cerate_url = reverse('profile')
        response = self.client.post(profile_cerate_url,{profile_pic:profile_pic, phonenum:phonenum, balance:balance, account_type:account_type, state:state, city:city, branch_name:branch_name})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'MyApp/profile.html')  

    def test_Customerinfo_get(self):
        self.client.login(username='chetan', password='demo')
        response = self.client.get(reverse('customer_info', args=[1]))
        self.assertEqual(response.status_code, 200)        

    def test_Customerinfo_post(self):
        self.client.login(username='chetan', password='demo')
        response = self.client.post(reverse('customer_info', args=[1]))
        self.assertEqual(response.status_code, 200)  

    def test_transfer_post(self, accno='Tanuj007', amount='500000', pin='pin' ):
        self.client.login(username='chetan', password='demo')
        transfer_cerate_url = reverse('transfer')
        response = self.client.post(transfer_cerate_url ,{accno:accno, amount:amount , pin:pin})
        self.assertEqual(response.status_code, 200)   
        self.assertTemplateUsed(response, 'MyApp/transfer.html') 


    def test_request_post(self, accno='accno', amount='amount', pin='pin' ):
        self.client.login(username='chetan', password='demo')
        request_cerate_url = reverse('requestmoney')
        response = self.client.post(request_cerate_url ,{accno:accno, amount:amount , pin:pin})
        self.assertEqual(response.status_code, 200)   
        self.assertTemplateUsed(response, 'MyApp/requestMoney.html') 

    def test_notification_post(self, user='accno', notification='amount'):
        self.client.login(username='chetan', password='demo')
        notification_cerate_url = reverse('notification')
        response = self.client.post(notification_cerate_url ,{user:user, notification:notification})
        self.assertEqual(response.status_code, 200)   
        self.assertTemplateUsed(response, 'MyApp/see_notification.html')


# total 11 test casess are hear
# docker, CICD
