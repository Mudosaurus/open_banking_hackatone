from django.contrib import admin

from .consent_model import Consent
from .operation_type_model import OperationType
from .atomic_operation_model import AtomicOperation
from .transaction_model import Transaction
from .consent_scope_model import ConsentScope


admin.site.register(Consent, admin.ModelAdmin)
admin.site.register(OperationType, admin.ModelAdmin)
admin.site.register(AtomicOperation, admin.ModelAdmin)
admin.site.register(Transaction, admin.ModelAdmin)
admin.site.register(ConsentScope, admin.ModelAdmin)
