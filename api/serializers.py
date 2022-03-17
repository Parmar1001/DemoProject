from rest_framework import serializers
from MyApp.models import Customer, Notification, Contact, Branch


class BranchSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Branch
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Notification
        fields = '__all__'



class ContactSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    
    class Meta:
        model = Contact
        fields = '__all__'




