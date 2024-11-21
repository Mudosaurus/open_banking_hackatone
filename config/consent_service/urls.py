from rest_framework import routers
from django.views.defaults import permission_denied
from django.urls import include, path

from .consent_view import ConsentViewSet
from .operation_type_view import OperationTypeViewSet
from .atomic_operation_view import AtomicOperationViewSet
from .transaction_view import TransactionViewSet


router = routers.DefaultRouter()
router.register(r'consent', ConsentViewSet)
router.register(r'operation_type', OperationTypeViewSet)
router.register(r'atomic_operation', AtomicOperationViewSet)
router.register(r'transaction', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls))
]
