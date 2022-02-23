from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Branch(models.Model):
    name = models.CharField(primary_key=True,max_length=20)# True will make the field PRIMARY KEY for that table (model) or Django will automatically add an AutoField.
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)# AutoField is an IntegerField that automatically increments according to available IDs.
    # we also use hear, (auto_created = True,serialize = False, verbose_name ='ID')
    user_name=models.OneToOneField(User,on_delete=models.CASCADE)#links the User model to another model that contains additional fields (this can also be referred to as a User Profile).
    date_of_open=models.DateTimeField(auto_now_add=True)
    balance=models.FloatField()
    account_type=models.CharField(max_length=20)
    branch_name=models.ForeignKey(Branch,on_delete=models.CASCADE)# Many-to-one relationships by adding Foreignkey.
    city=models.CharField(max_length=30,default=None)
    state=models.CharField(max_length=30,default=None)
    phonenum=models.CharField(max_length=10)
    profile_pic=models.ImageField(default=None)    

class Notification(models.Model):
    notification_id=models.AutoField(primary_key=True)
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    notification=models.CharField(max_length=200,default=None)

