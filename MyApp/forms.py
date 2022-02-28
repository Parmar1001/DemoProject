from django import forms
from django.contrib.auth.models import User
from MyApp.models import Customer

class SignUpForm(forms.ModelForm):
    class Meta: 
        model=User
        fields=['username','password','email','first_name','last_name']
        
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['profile_pic','balance','account_type','state','city','branch_name']


class TransferForm(forms.Form):
    account=forms.CharField(label='To account number',max_length=10)
    amount=forms.FloatField(label='Amount to be transfered')
    pin=forms.CharField(max_length=20,label='Your pin')


class RequestForm(forms.Form):
    account=forms.CharField(label='Frequest from user',max_length=10)
    amount=forms.FloatField(label='Request Amount')
    pin=forms.CharField(max_length=20,label='Your pin')