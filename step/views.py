from django.shortcuts import render
from.models import Supplier,Business,Customer,Products,Purchase
from .forms import SupplierForm,Businessform,CustomerForm,testform,ProductForm,PurchaseForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
#main styling
def index(request):
    return render(request,'step/index.html')

def home(request):
    user = request.user
    return render(request,"step/home.html",{"user":user})




#used to run test
def test(request):
    return render(request,"step/test.html",{"form":testform})



#used to show all the suppliers
@login_required()
def supplier(request):
     #get all the business the user owns
     user_businesses = request.user.business_set.all()
     #retrieve all the suppliers associated with the users business
     suppliers = Supplier.objects.filter(business__in=user_businesses)

     return render(request,'step/suppliers.html',{'suppliers':suppliers})

#used to show all the customers
def customers(request):

    user_customer = request.user.business_set.all()
    customers = Customer.objects.filter(business__in=user_customer)

    return render(request,'step/customer.html',{'customers':customers})

#used to show all the products
def products(request):
     products = Products.objects.filter(user=request.user)
     return render(request,'step/products.html',{"products":products})

def purchase(request):
    purchase = Purchase.objects.filter(user=request.user)
    return render(request,'step/purchase.html',{"purchases":purchase})



#used to add new customers 
@login_required()
def add_customer(request):
    #check if user is logged in

    if request.user.is_authenticated:
        if request.method=='POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                form.save()

                return render(request,'step/add_customers.html',{'form':CustomerForm, 'success':True})
        else:
            user_business = Business.objects.filter(user=request.user)
            form = CustomerForm(initial={'business': user_business.first()})
            return render(request,'step/add_customers.html',{'form':form})


@login_required()
def add_purchase(request):
    if request.user.is_authenticated:
     if request.method=='POST':
        form = PurchaseForm(request.POST)

        if form.is_valid():
            new_purchase = form.save(commit=False)
            new_purchase.user=request.user

            #Get the product the purchase is made for a
            product_purchased = new_purchase.product
            #Get the quantity of the product purchased 
            quantity_purchased = new_purchase.quantity

            print(quantity_purchased)
            #Get the product quatinty for the product purchases
            update_quantity = Products.objects.get(pk=product_purchased.pk)

            update_quantity.stock += quantity_purchased

            update_quantity.save()
            

           
           


            new_purchase.save()

            return render(request,'step/add_purchases.html',{"form":PurchaseForm(),"success":True})
     else:

        return render(request,'step/add_purchases.html',{"form":PurchaseForm()})







#used to add suppliers 
@login_required()
def add_supplier(request):

   if request.user.is_authenticated:
     if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
           new_supplier = form.save(commit=False)
           if request.user.business_set.exists():
                new_supplier.business = request.user.business_set.first()
                new_supplier.save() 

                return render(request, 'step/add_suppliers.html', {'form': SupplierForm(), 'success': True})

     else:
        user_businesses = Business.objects.filter(user=request.user)
        form = SupplierForm(initial={'business': user_businesses.first()}) # Corrected instantiation of the form
        return render(request, 'step/add_suppliers.html', {'form': form})
     

#used to add products
@login_required()
def add_product(request):
    if request.user.is_authenticated:
        if request.method =='POST':
        
            form = ProductForm(request.POST)
            if form.is_valid():
               new_product=form.save(commit=False)
               new_product.user=request.user
               new_product.save()
               return render(request,'step/add_product.html',{"form":form,"success":True})

    return render(request,'step/add_product.html',{"form":ProductForm()})

#used to add businesses 
@login_required()
def add_business(request):
    if request.method == 'POST':
        form = Businessform(request.POST)
        if form.is_valid():
             new_business=form.save(commit=False)
             new_business.user = request.user  # Associate with logged-in user
             new_business.save()        

             return render(request,'step/add_business.html',{'form':form})
    else:
        form = Businessform
        return render(request,'step/add_business.html',{'form':form})
    

#need to fic this
def delete(request,id):
    if request=='POST':
        s = Customer.objects.get(pk=id)
        s.delete()
        
        user_customer = request.user.business_set.all()
        customers = Customer.objects.filter(business__in=user_customer)
        return render(render,'step/customer.html',{"customers":customers})
    else:
      return HttpResponseRedirect(reverse('customer'))


def edit(request,id):
    if request.method=='POST':
       customer = Customer.objects.get(pk=id)
       form=CustomerForm(request.POST,instance=customer)
       if form.is_valid():
           form.save()

           return render(request,'step/customer_edit.html',{"form":form})
    else:
       customer = Customer.objects.get(pk=id)
       form = CustomerForm(instance=customer)
       return render(request, 'step/customer_edit.html', {
    'form': form
    })


