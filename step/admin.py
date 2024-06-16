from django.contrib import admin
from.models import Business,Supplier,Customer,Products,Purchase,Status,sells,mode_of_payment,Expense_category,expenses,notifications,payment_status,Transactions

admin.site.register(Business)
admin.site.register(Supplier)
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Purchase)
admin.site.register(Status)
admin.site.register(sells)
admin.site.register(mode_of_payment)
admin.site.register(Expense_category)
admin.site.register(expenses)
admin.site.register(notifications)
admin.site.register(payment_status)
admin.site.register(Transactions)
