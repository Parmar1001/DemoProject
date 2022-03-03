from django.urls import path
from . import views

urlpatterns = [
    path('Home/', views.HomeView,name="Home"),
    # path('signup/', views.SignupView,name='signup'),
    # path('customerinfo/', views.CustomerInfo),
    # path('transfer/',views.TransferMoney),
    # path('requestmoney/',views.RequestMoney),
    # path('notification/',views.NotificationView), 
    # path('contact/',views.ContactView.as_view(),name="contact"),
    # path('service/',views.ServiceView,name="service"),
    # path('about/',views.AboutView,name="about"),
    # path('clients/',views.ClientsView,name="clients"),
]