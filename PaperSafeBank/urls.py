from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('MyApp/',include('MyApp.urls')),
    path('account/',include('django.contrib.auth.urls')),
]