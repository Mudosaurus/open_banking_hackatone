from django.http import HttpResponse, Http404, HttpResponseServerError
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from .transaction_model import Transaction, TransactionSerializer
from .atomic_operation_model import AtomicOperation


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    
id_param = openapi.Parameter('id', openapi.IN_HEADER, description="transaction id", type=openapi.FORMAT_UUID)

    
@swagger_auto_schema(method='post', manual_parameters=[id_param])
@api_view(['POST'])
def start_transaction(request):    
    try:
        transaction = get_object_or_404(Transaction, pk=request.headers.get('id'))
    except ValidationError as ex:
        raise Http404(str(ex))
    
    operations = AtomicOperation.objects.filter(transaction_id=transaction.id)

    for operation in operations:
        try:
            operation.start()
        except Exception as ex:
            return HttpResponseServerError(ex)
                    
    response = HttpResponse(content='Ok')
    #     headers={
    #         'State': transaction.,
    #         'Id': request.headers['id']
    #     }
    # )
    
    return response
