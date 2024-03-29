from django import forms
from.models import Supplier,Business,Customer,test,Products,Purchase


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['business','supplier_name','location','phone_number']
       



class Businessform(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['business_name']
    

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields= ['business','first_name','last_name','phone_number','opening_credit']



class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields=['product_name','supplier','Buying_price','selling_price','alert_quantity','stock']

class testform(forms.ModelForm):
    class Meta:
        model = test
        fields = ['pic']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        #fields=['supplier','product','Buying_price','date','status','quantity']
        fields='__all__'