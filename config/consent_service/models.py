from django.contrib.postgres.fields import ArrayField
from django.db import models


class Consent(models.Model):
    zone = models.CharField(max_length=255)
    organizations = ArrayField(models.CharField(max_length=255), blank=False)
    agreement = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.zone}: {self.agreement} from organization {self.organizations}'

    class Meta:
        verbose_name = 'consent'
        verbose_name_plural = 'consents'
        ordering = ('zone','agreement',)
