from django.core.exceptions import AppRegistryNotReady
from django.db.models.aggregates import Count
from django.core import serializers
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
from product.models import (
    Product, 
    Warehouse,
    CompartmentProduct
    )
from product.serializers import (
    ProductSerializer, 
    WarehouseSerializer,
    AddProductSerializer
)

class ProductsView(APIView):
    product_serializer = ProductSerializer
    def get(self, request, format=None):
        product_list = Product.objects.all()
        serializer = self.product_serializer(product_list, many=True)
        serialized_data = serializer.data
        return Response(serialized_data)

    def post(self, request, format=None):
        serializer = self.product_serializer(request.data)

        if serializer.is_valid():
            serializer.save()
            product_information = serializer.data
            return Response(product_information, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):
    product_serializer = ProductSerializer

    def get_product(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        serialized_product = self.product_serializer(self.get_product(pk))
        data = serialized_product.data
        return Response(data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        product_object = self.get_product(pk)
        serializer = self.product_serializer(product_object, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        product_object = self.get_product(pk)
        product_object.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)        

class WarehouseCreateView(APIView):
    warehouse_serializer = WarehouseSerializer
    def post(self, request, format=None):
        serializer = self.warehouse_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WarehouseAddProductView(APIView):
    addproduct_serializer = AddProductSerializer
    def post(self, request, format=None):
        serializer = self.addproduct_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WarehouseRemoveProductView(APIView):
    def delete(self, request, pk, format=None):
        product_object = self.get_product(pk)
        product_object.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)        

class WarehousesView(APIView):
    warehouse_view_serializer = AddProductSerializer
    def get(self, request, format=None):
        product_list = CompartmentProduct.objects.values('compartment_id','product_id').annotate(pcount=Count('product_id')).order_by()
        # serializer = self.warehouse_view_serializer(product_list, many=True)
        # serialized_data = serializer.data

        return Response(product_list)

   

class WarehouseView(APIView):
    warehouse_view_serializer = AddProductSerializer
    def get_warehouse(self, pk):
        try:
            return Warehouse.objects.get(pk=pk)
        except CompartmentProduct.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        warehouse_id = self.get_warehouse(pk)
        serialized_product = CompartmentProduct.objects.filter(warehouse_id=warehouse_id)
        data = serializers.serialize('json',serialized_product)
        return Response(data, status=status.HTTP_200_OK)
    
