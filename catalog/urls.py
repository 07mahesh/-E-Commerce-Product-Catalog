from django.urls import path
from . import views

urlpatterns = [
    path('product_list/',views.product_list,name='product_list'),
    path('product_detail/<int:product_id>',views.product_detail,name='product_detail')
]