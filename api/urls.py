from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
# from rest_framework.authtoken.views import obtain_auth_token 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Creating Router Object
router = routers.DefaultRouter()

# Register with Router
router.register(r'Branch', views.BranchViewSet)
router.register(r'Customer', views.CustomerViewSet)
router.register(r'Notification', views.NotificationViewSet)
router.register(r'Contact', views.ContactViewSet)

schema_view = get_schema_view(
      openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="chparmar@bestpeers.com"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('Branch', views.BranchViewSet, name='Branch'),
    path('Customer', views.CustomerViewSet, name='Customer'),
    path('Notification', views.NotificationViewSet, name='Notification'),
    path('Contact', views.ContactViewSet, name='Contact'),
]




