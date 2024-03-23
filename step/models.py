from django.db import models
from django.contrib.auth.models import User




class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)  # Foreign key to User
    business_name = models.CharField(max_length=200)
    # ... Other business fields

    def __str__(self):
        return self.business_name
    

class Business_location(models.Model):
    Business = models.ForeignKey(Business,on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    phone_number  = models.IntegerField()






class Supplier(models.Model):
    business = models.ForeignKey(Business,on_delete=models.CASCADE,null=True)
    supplier_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
   

    def __str__(self) -> str:
        return f'supplier {self.supplier_name}'










class Customer(models.Model):
    business = models.ForeignKey(Business,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    opening_credit = models.IntegerField(default=0)
   

    def __str__(self) -> str:
        return f'customer  {self.first_name}'
    

class Products(models.Model):
      product_name=models.CharField(max_length=200)
      supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
      Buying_price = models.IntegerField()
      selling_price = models.IntegerField()
      alert_quantity = models.IntegerField(default=3)
      stock = models.IntegerField(null=False)
      product_picture = models.ImageField(upload_to='images')

      def __str__(self) -> str:
        return  self.product_name




class test(models.Model):
    pic = models.ImageField()






    

