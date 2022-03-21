from rest_framework import serializers
from MyApp.models import Customer, Notification, Contact, Branch


class BranchSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Branch
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        user = self.context["request"].user
        return self.Meta.model.objects.create(user=user, **validated_data)


class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Notification
        fields = '__all__'
    
    def create(self, validated_data):
        user = self.context["request"].user
        return self.Meta.model.objects.create(user=user, **validated_data)


class ContactSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source="user.username", read_only=True)
    
    class Meta:
        model = Contact
        fields = '__all__'




