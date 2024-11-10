from django.contrib import admin
from . import models


class TestModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.TestModel, TestModelAdmin)
admin.site.register(models.Client, admin.ModelAdmin)
admin.site.register(models.Valute, admin.ModelAdmin)
admin.site.register(models.Account, admin.ModelAdmin)
