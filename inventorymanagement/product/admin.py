from django.contrib import admin

from product.models import Product, Warehouse, Compartments, CompartmentProduct
# Register your models here.

admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(Compartments)
admin.site.register(CompartmentProduct)
