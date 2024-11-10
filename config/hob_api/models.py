from django.db import models

from .money_field import MoneyField
        
        
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
    balance = MoneyField()

    def __str__(self):
        return f'Account of {self.holder} in {self.valute.code}'

    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'
    
    
class Loan(models.Model):
    borrower = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    credit_sum = MoneyField()
    pay_rest = MoneyField()
    monthly_pay = MoneyField()
    get_date = models.DateField(blank=False, null=False)
    repayment_date = models.DateField(blank=False, null=False)
    documents = models.TextField()
    
    def __str__(self):
        return f'Loan of {self.borrower} from {self.get_date}'    
    
    class Meta:
        verbose_name = 'loan'
        verbose_name_plural = 'loans'
        ordering = ('get_date',)


class Salary(models.Model):
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    date_time = models.DateTimeField(blank=False, null=False)
    sum = MoneyField()
    category = models.CharField(max_length=255, blank=False)
    type = models.CharField(max_length=10, blank=False)
    
    def __str__(self):
        return f'{self.type} {self.category} of {self.account} at {self.date_time}'

    class Meta:
        verbose_name = 'salary'
        verbose_name_plural = 'salaries'
        ordering = ('date_time',)
