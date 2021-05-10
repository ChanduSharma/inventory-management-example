from rest_framework import serializers
from product.models import Product, Warehouse, CompartmentProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompartmentProduct
        fields = '__all__'
