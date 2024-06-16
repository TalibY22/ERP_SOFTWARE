from django.contrib import admin
from django.urls import path,include
from . import views 
from django.conf import settings

from django.conf.urls.static import static






urlpatterns = [
 path("", views.home,name="home"),
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
  path("purchase/add",views.add_purchase,name="add_purchase"),
  path("customer/edit/<int:id>",views.edit,name="customer_edit"),
  path("sell/add",views.add_sales,name="add_sales"),
  path("sells/",views.sales,name="sales"),
  path("expenses/",views.expenses1,name="expenses"),
  path("expenses/add",views.add_expense,name="add_expense"),
  path("notifications/",views.notify,name='notify'),
  path("transactions/",views.view_transaction,name='transaction'),


  path("delete/<int:model>/<int:id>/",views.delete_customer,name="delete_customer"),
  path("search/",views.search,name="search"),
  path("pos/",views.pos,name="pos"),
  path("transaction/<int:id>",views.transaction,name='transaction'),


  path("stk/",views.initiate_stk_push,name="stk_push"),
  path("callback/",views.mpesa_callback,name="callback")
  

#<td>
              #<img src="{{ MEDIA_URL }}{{ product.product_picture.url }}" alt="{{ product.product_name }} image" width="50" height="50">
            #</td>..>

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
