from django.urls import path
from . import views

urlpatterns = [
    path('', views.ConsentViewSet.as_view()),
]