from django import forms
from django.contrib.auth.models import User
from MyApp.models import Customer
from allauth.account.forms import SignupForm


# class SignupForm(SignupForm):

#     def signup(self, *args, **kwargs):
#         class Meta: 
#             model=User, Customer
#             fields=['username','password','email','first_name','last_name','profile_pic','balance','account_type','state','city','branch_name']
#         return super(SignupForm, self).signup(*args, **kwargs)


# class SignUpForm(forms.ModelForm):
#     class Meta: 
#         model=User
#         fields=['username','password','email','first_name','last_name']
#         #fields='__all__'
        
        
# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model=Customer
#         fields=['profile_pic','balance','account_type','state','city','branch_name']


class TransferForm(forms.Form):
    accno=forms.CharField(label='To account number',max_length=10)
    amount=forms.FloatField(label='Amount to be transfered')
    pin=forms.CharField(max_length=20,label='Your pin')

    
class RequestForm(forms.Form):
    accno=forms.CharField(label='Frequest from user',max_length=10)
    amount=forms.FloatField(label='Request Amount')
    pin=forms.CharField(max_length=20,label='Your pin')

