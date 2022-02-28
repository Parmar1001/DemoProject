from django.urls import path
from . import views
urlpatterns = [
    path('Home/', views.home_view),
    path('signup/', views.signup_view,name='signup'),
    path('customerinfo/', views.customerInfo),
    path('transfer/',views.transfer_view),
    path('requestmoney/',views.requestMoney_view),
]