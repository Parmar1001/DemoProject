from django.urls import path
from . import views
urlpatterns = [
    path('Home/', views.home_view),
    path('signup/', views.signup_view,name='signup'),
    path('customerinfo/', views.customerInfo),
    path('transfer/',views.transfer_view),
    path('requestmoney/',views.requestMoney_view),
    path('notification/',views.notification_view), 
    path('contact/',views.contact_view,name="contact"),
    path('service/',views.service_view,name="service"),
    path('about/',views.about_view,name="about"),
    path('clients/',views.clients_view,name="clients"),
]