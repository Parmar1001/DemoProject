from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="Home"),
    path("profile", views.ProfileView.as_view(), name="profile"),
    path("customer_info/<int:pk>", views.CustomerInfo, name="customer_info"),
    path("transfer/", views.TransferView, name="transfer"),
    path("requestmoney/", views.RequestMoneyView, name="requestmoney"),
    path("notification/", views.NotificationView, name="notification"),
    path("service/", views.ServiceView, name="service"),
    path("about/", views.AboutView, name="about"),
    path("clients/", views.ClientsView, name="clients"),
    path("contact/", views.contactView.as_view(), name="contact"),
]