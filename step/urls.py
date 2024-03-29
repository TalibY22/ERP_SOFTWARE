from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
 path("", views.index,name="Index"),
 path("supplier/",views.supplier,name="supplier"),
  path("supplier/add",views.add_supplier,name="add_supplier"),
  path("add_business/",views.add_business,name="add_business"),
  path("test/",views.test,name="test"),
  path("add_customer/",views.add_customer,name="add_customer"),
  path("customer/",views.customers,name="customer"),
  path("add_product/",views.add_product,name="add_product"),
  path("delete/<int:id>",views.delete,name="delete"),
  path("products/",views.products,name="products"),
  path("purchase/",views.purchase,name="purchase"),
  path("purchase/add",views.add_purchase,name="add_purchase")

#<td>
              #<img src="{{ MEDIA_URL }}{{ product.product_picture.url }}" alt="{{ product.product_name }} image" width="50" height="50">
            #</td>..>

]
