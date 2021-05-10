from django.urls import path
from product.views import (
    ProductsView,
    ProductView,
    WarehouseCreateView,
    WarehouseAddProductView,
    WarehouseRemoveProductView,
    WarehousesView,
    WarehouseView
)

urlpatterns = [
    path('api/products', ProductsView.as_view()),
    path('api/product/<int:pk>/', ProductView.as_view()),
    path('api/warehouse/create', WarehouseCreateView.as_view()),
    path('api/warehouse/addproduct',WarehouseAddProductView.as_view()),
    path('api/warehouse/removeproduct', WarehouseRemoveProductView.as_view()),
    path('api/warehouses', WarehousesView.as_view()),
    path('api/warehouse/<int:pk>/', WarehouseView.as_view())
]
