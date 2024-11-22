from typing import Any

from django.db.models import BigIntegerField


class MoneyField(BigIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['default'] = 0
        super().__init__(*args, **kwargs)

    def deconstruct(self) -> Any:
        name, path, args, kwargs = super().deconstruct()
        del kwargs["default"]
        return name, path, args, kwargs
