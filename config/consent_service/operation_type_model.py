from bank_api.models import OperationType
from bank_api.serializers import OperationTypeSerializer

APP_LABEL = 'consent_service'


class ConsentOperattionType(OperationType):
    class Meta(OperationType.Meta):
        app_label = APP_LABEL


class ConsentOperationTypeSerializer(OperationTypeSerializer):
    class Meta(OperationTypeSerializer.Meta):
        model = ConsentOperattionType
