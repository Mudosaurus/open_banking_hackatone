# from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from . import serializers
from . import models


class TestModelViewSet(ModelViewSet):
    queryset = models.TestModel.objects.all()
    serializer_class = serializers.TestModelSerializer
    