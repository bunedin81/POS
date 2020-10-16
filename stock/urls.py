from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.product_list, name='product-list'),
    path('product_create/', views.create_product, name='product-create'),
    path('product_update/', views.update_product, name='product-update'),
]