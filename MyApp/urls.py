from django.urls import path
from . import views
urlpatterns = [
    path('Home/', views.home_view),
    path('signup/', views.signup_view),
    path('customerinfo/', views.customerInfo),
]