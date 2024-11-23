from django.http import HttpResponse, Http404, HttpResponseServerError
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from rest_framework.request import Request


operation_type_param = openapi.Parameter('operation-type', openapi.IN_HEADER, description="operation type", type=openapi.TYPE_STRING)
operation_details_param =  openapi.Parameter('operation-details', openapi.IN_HEADER, description="operation details", type=openapi.TYPE_OBJECT)
    
@swagger_auto_schema(method='post', manual_parameters=[operation_type_param, operation_details_param])
@api_view(['POST'])
def execute_operation(request: Request, **kwargs):
    operation_type = request.headers.get('operation-type')
    operation_details = request.headers.get('operation-details')
    
    try:
        operation_details = eval(operation_details)
    except TypeError:
        operation_details = {}
    
    operation_type_model = kwargs.get('operation_type_model')    
    operation_model = kwargs.get('operation_model')
    account_model = kwargs.get('account_model')
    
    try:
        operation_type_obj = get_object_or_404(operation_type_model, pk=operation_type)
        account_obj = get_object_or_404(account_model, pk=operation_details.get('account'))
    except ValidationError as ex:
        raise Http404(str(ex))
    
    try:
        operation = operation_model(operation_type=operation_type_obj,
                                    account=account_obj,
                                    sum=operation_details.get('sum'))
    except ValueError as ex:
        raise Http404(str(ex))
    
    operation.save()   
    
    try:  
        operation.execute()   
    except Exception as ex:
        return HttpResponseServerError(ex)
        
    response = HttpResponse(content='Ok - bank')    
    return response
