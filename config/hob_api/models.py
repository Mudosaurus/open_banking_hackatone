from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'test_model'
        verbose_name_plural = 'test_models'
        ordering = ('name',)
