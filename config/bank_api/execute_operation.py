from django.http import HttpResponse, Http404, HttpResponseServerError
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

id_param = openapi.Parameter('id', openapi.IN_HEADER, description="transaction id", type=openapi.FORMAT_UUID)

    
@swagger_auto_schema(method='post', manual_parameters=[id_param])
@api_view(['POST'])
def execute_operation(request):    
    # try:
    #     pass
    #     # transaction = get_object_or_404(Transaction, pk=request.headers.get('id'))
    # except ValidationError as ex:
    #     raise Http404(str(ex))
                        
    response = HttpResponse(content='Ok - bank')
    
    return response
