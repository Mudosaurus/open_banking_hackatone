import sys
import inspect
from django.contrib import admin    


def register_api_to_admin(models_module_name):
    models = [cls for _, cls in inspect.getmembers(sys.modules[models_module_name], inspect.isclass) if cls.__module__ == models_module_name]
    admin.site.register(models, admin.ModelAdmin)
