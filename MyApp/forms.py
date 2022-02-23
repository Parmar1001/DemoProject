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