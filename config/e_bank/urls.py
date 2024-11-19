from django.urls import path, include

from hob_api.services import get_router

urlpatterns = [
    path('', include(get_router().urls)),
]
