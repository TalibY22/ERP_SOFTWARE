from django import forms
from.models import Supplier,Business,Customer,test,Products,Purchase,sells,expenses


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
        fields=['product_name','supplier','Buying_price','selling_price','alert_quantity','stock','product_picture']
        product_picture = forms.ImageField()
        #fields='__all__'


class SellForm(forms.ModelForm):
    class Meta:
        model = sells
        fields = ['customer','Product_sold','mode_of_payment','quantity_sold','Payment_status']



class testform(forms.ModelForm):
    class Meta:
        model = test
        fields = ['pic']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields=['supplier','product','Buying_price','status','quantity']
        

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = expenses 
        fields='__all__'