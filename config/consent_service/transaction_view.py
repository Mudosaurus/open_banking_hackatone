from django.http import HttpResponse
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.viewsets import ModelViewSet
from .transaction_model import Transaction, TransactionSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    
id_param = openapi.Parameter('id', openapi.IN_HEADER, description="transaction id", type=openapi.TYPE_STRING)

    
@swagger_auto_schema(method='post', manual_parameters=[id_param])
@api_view(['POST'])
def start_transaction(request):
    response = HttpResponse(
        headers={
            'State': 'Test',
            'Id': request.headers['id']
        }
    )
    
    return response
