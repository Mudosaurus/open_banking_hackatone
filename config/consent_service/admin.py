from django.contrib import admin

from .consent_model import Consent
from .operation_type_model import OperationType
from .atomic_operation_model import AtomicOperation
from .transaction_model import Transaction


admin.site.register(Consent, admin.ModelAdmin)
admin.site.register(OperationType, admin.ModelAdmin)
admin.site.register(AtomicOperation, admin.ModelAdmin)
admin.site.register(Transaction, admin.ModelAdmin)
