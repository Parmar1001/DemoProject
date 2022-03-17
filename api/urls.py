from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token 

# Creating Router Object
router = routers.DefaultRouter()

# Register with Router
router.register(r'Branch', views.BranchViewSet)
router.register(r'Customer', views.CustomerViewSet)
router.register(r'Notification', views.NotificationViewSet)
router.register(r'Contact', views.ContactViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

#Token f0bebd136ef541ae4fa618573928a59f974a852d
