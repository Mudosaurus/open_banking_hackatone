from django.urls import include, path

from hob_api.services import get_router

urlpatterns = [
    path('', include(get_router().urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
