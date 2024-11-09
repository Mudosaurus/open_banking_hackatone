from rest_framework.generics import ListAPIView
from . import serializers
from . import models


class TestModelListAPIView(ListAPIView):
    serializer_class = serializers.TestModelSerializer

    def get_queryset(self):
        return models.TestModel.objects.all()
