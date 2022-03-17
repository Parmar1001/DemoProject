from MyApp.models import Customer, Branch, Notification, Contact
from rest_framework import viewsets #permissions
 
from .serializers import CustomerSerializer, BranchSerializer, NotificationSerializer, ContactSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.IsAuthenticated]


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.IsAuthenticated]


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.IsAuthenticated]

