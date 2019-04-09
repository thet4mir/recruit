from django.db import models
from django.utils import timezone

# Create your models here.

class Drug_category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Drug_order_status(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Drug_detail(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    nairlaga = models.CharField(max_length=100)
    intro = models.CharField(max_length=100)
    other_side = models.CharField(max_length=100)
    zaavar = models.CharField(max_length=100)
    age = models.IntegerField()
    duration = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    factory = models.CharField(max_length=100)
    price = models.IntegerField()
    drug_catedory = models.ForeignKey(Drug_category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Drug_add(models.Model):
    date = models.DateField(default=timezone.now)
    about = models.CharField(max_length=100)
    drug_detail = models.ForeignKey(Drug_detail, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.drug_detail.name

class Drug_order(models.Model):
    date = models.DateField(default=timezone.now)
    number = models.IntegerField()
    recived_date = models.DateField(default=timezone.now)
    about = models.CharField(max_length=100)
    drug_add = models.ForeignKey(Drug_add, on_delete=models.SET_NULL, null=True, blank=True)
    drug_order_status = models.ForeignKey(Drug_order_status, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.date
