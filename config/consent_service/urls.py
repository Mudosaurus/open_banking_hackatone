from rest_framework import routers
from django.urls import include, path

from .consent_view import ConsentViewSet
from .operation_type_view import OperationTypeViewSet
from .atomic_operation_view import AtomicOperationViewSet
from .transaction_view import TransactionViewSet, start_transaction
from .consent_scope_view import ConsentScopeViewSet


router = routers.DefaultRouter()
router.register(r'consent', ConsentViewSet)
router.register(r'operation_type', OperationTypeViewSet)
router.register(r'atomic_operation', AtomicOperationViewSet)
router.register(r'transaction', TransactionViewSet)
router.register(r'consent_scope', ConsentScopeViewSet)

urlpatterns = [
    path('api/start_transaction', start_transaction, name='start_transaction'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
