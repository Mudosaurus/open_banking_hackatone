from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'test_model'
        verbose_name_plural = 'test_models'
        ordering = ('name',)
        
        
class Client(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=True)
    family_name = models.CharField(max_length=255, blank=False)    
    
    def __str__(self):
        return f'{self.first_name} {self.family_name} {self.last_name}'

    class Meta:
        verbose_name = 'client of the bank'
        verbose_name_plural = 'clients of the bank'
    
    
class Valute(models.Model):
    code = models.CharField(max_length=3, blank=False)
    name = models.CharField(max_length=255, blank=False)
    
    def __str__(self) -> str:
        return self.code
    
    class Meta:
        verbose_name = 'valute'
        verbose_name_plural = 'valutes'
        ordering = ('code',)
    

class Account(models.Model):
    holder = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    valute = models.ForeignKey(Valute, on_delete=models.DO_NOTHING)    
    balance = models.BigIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return f'Account of {self.holder} in {self.valute.code}'

    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'
    