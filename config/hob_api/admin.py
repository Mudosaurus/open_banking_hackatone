from django.contrib import admin
from . import models


class TestModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.TestModel, TestModelAdmin)
