from django.urls import path
from . import views


urlpatterns = [
    path('test_models', views.TestModelListAPIView.as_view(), name='api_test_models'),
]
