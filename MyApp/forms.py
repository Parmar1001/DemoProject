from distutils.command.upload import upload
from django import forms
from django.contrib.auth.models import User
from MyApp.models import Customer
from django.contrib.auth.forms import UserCreationForm

# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     class Meta:
#         model=User
#         fields=['username','password','email','first_name','last_name']


from allauth.account.forms import SignupForm

# class MyCustomSignupForm(SignupForm):
#     balance=forms.CharField(label='Balance',max_length=10)
#     branch=forms.CharField(label='Branch Name',max_length=50)
#     ACCOUNT_CHOICE = (
#         ('Saving','Saving'),('Current','Current')
#     )
#     account=forms.ChoiceField(label='Account Type',choices=ACCOUNT_CHOICE)
#     CITY_CHOICES= (
#         ('Indore','Indore'),('Dewas','Dewas'),('Mhow','Mhow'),('Bhopal','Bhopal')
#     )
#     city=forms.ChoiceField(label='City',choices=CITY_CHOICES)
#     state=forms.CharField(label='State',max_length=50)
#     profile=forms.ImageField(label='Upload Pic' ,required=False,)
#     def save(self, request):
#         user = super(MyCustomSignupForm, self).save(request)
#         c = Customer(balance=self.cleaned_data['balance'],branch=self.cleaned_data['Branch Name'],account=self.cleaned_data['Account Type'],city=self.cleaned_data['City'],state=self.cleaned_data['State'],profile=self.cleaned_data['Upload Pic'],user_name=user)
#         c.save()
#         return user

# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model=Customer
#         fields=['profile_pic','balance','account_type','state','city','branch_name']


class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")

    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class TransferForm(forms.Form):
    accno = forms.CharField(label="To account number", max_length=10)
    amount = forms.FloatField(label="Amount to be transfered")
    pin = forms.CharField(max_length=20, label="Your pin")


class RequestForm(forms.Form):
    accno = forms.CharField(label="Frequest from user", max_length=10)
    amount = forms.FloatField(label="Request Amount")
    pin = forms.CharField(max_length=20, label="Your pin")


class EmailSendForm(forms.Form):
    name=forms.CharField()
    to=forms.EmailField()
