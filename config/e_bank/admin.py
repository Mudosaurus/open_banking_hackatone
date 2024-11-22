from bank_api.admin import register_api_to_admin
from . import models


register_api_to_admin(models.__name__)
