from typing import ClassVar
from django.db import models
import uuid
from enum import Enum
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Product(models.Model):
    class StorageType(models.TextChoices):
        NORMAL = 'N', _('Normal')
        COLD = 'C', _('Cold')
        HAZARD = 'H', _('Hazard')
    sku_id = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250)
    price_in_usd = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=100)
    storage_type = models.CharField(
        max_length=1, 
        choices=StorageType.choices, 
        default=StorageType.NORMAL
    )
    is_archived = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Warehouse(models.Model):
    warehouse_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.warehouse_name

class Compartments(models.Model):

    class CompartmentType(models.TextChoices):
        AVAILABLE = 'A', _('Available')
        DAMAGED = 'D', _('Damaged')
        RESERVED = 'R', _('Reserved')
    compartment_type = models.CharField(
        max_length=1, 
        choices=CompartmentType.choices, 
        default=CompartmentType.AVAILABLE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.compartment_type

class CompartmentProduct(models.Model):
    compartment_id = models.ForeignKey(Compartments, on_delete=models.CASCADE)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,  on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
