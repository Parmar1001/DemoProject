from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Branch(models.Model):
    branch_name=models.CharField(primary_key=True,max_length=20)
    branch_city=models.CharField(max_length=20)
    branch_state=models.CharField(max_length=30)
    

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    user_name=models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_open=models.DateTimeField(auto_now_add=True)
    balance=models.FloatField()
    account_type=models.CharField(max_length=20)
    branch_name=models.ForeignKey(Branch,on_delete=models.CASCADE)
    city=models.CharField(max_length=30,default=None)
    state=models.CharField(max_length=30,default=None)
    phonenum=models.CharField(max_length=10)
    profile_pic=models.ImageField(upload_to='static/images/',default=None)    

    

class Notification(models.Model):
    notification_id=models.AutoField(primary_key=True)
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    notification=models.CharField(max_length=200,default=None)
