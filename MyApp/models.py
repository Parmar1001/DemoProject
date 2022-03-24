from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Branch(models.Model):
    branch_name = models.CharField(primary_key=True, max_length=20)
    branch_city = models.CharField(max_length=20)
    branch_state = models.CharField(max_length=30)

    def __str__(self):
        return "{} branch, {} ,{}".format(
            self.branch_name, self.branch_city, self.branch_state
        )


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, related_name="customer", on_delete=models.CASCADE)
    date_of_open = models.DateTimeField(auto_now_add=True)
    balance = models.FloatField()
    ACCOUNT_CHOICE = (("Saving", "Saving"), ("Current", "Current"))
    account_type = models.CharField(
        max_length=20, choices=ACCOUNT_CHOICE, default="Saving"
    )
    branch_name = models.ForeignKey(
        Branch, related_name="customers", on_delete=models.CASCADE
    )
    CITY_CHOICES = (
        ("Indore", "Indore"),
        ("Dewas", "Dewas"),
        ("Mhow", "Mhow"),
        ("Bhopal", "Bhopal"),
    )
    city = models.CharField(max_length=30, default="Indore", choices=CITY_CHOICES)
    state_choices = (
        ("Madhya Pradesh", "Madhya Pradesh"),
        ("Maharashtra", "Maharashtra"),
        ("Manipur", "Manipur"),
        ("Meghalaya", "Meghalaya"),
        ("Mizoram", "Mizoram"),
    )
    state = models.CharField(
        choices=state_choices, max_length=255, default="Madhya Pradesh"
    )
    phonenum = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to="MyApp/sta", default=None)


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, related_name="notification", on_delete=models.CASCADE
    )
    notification = models.CharField(max_length=200, default=None)


class Contact(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    message = models.TextField(max_length=1000, blank=False)
    date = models.DateTimeField(default=timezone.now)
