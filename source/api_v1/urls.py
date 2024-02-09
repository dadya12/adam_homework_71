from django.urls import path, include
from rest_framework import routers
from api_v1.views import PubViewSet
from api_v1.views import get_token

app_name = 'api_v1'
router = routers.DefaultRouter()
router.register(r'publications', PubViewSet, basename='publications')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', get_token, name='token')
]

