from django.contrib import admin

from .consent_model import Consent
from .operation_type_model import ConsentOperattionType
from .atomic_operation_model import AtomicOperation
from .transaction_model import Transaction
from .consent_scope_model import ConsentScope
from .agent_model import Agent


admin.site.register(Consent, admin.ModelAdmin)
admin.site.register(ConsentOperattionType, admin.ModelAdmin)
admin.site.register(AtomicOperation, admin.ModelAdmin)
admin.site.register(Transaction, admin.ModelAdmin)
admin.site.register(ConsentScope, admin.ModelAdmin)
admin.site.register(Agent, admin.ModelAdmin)
