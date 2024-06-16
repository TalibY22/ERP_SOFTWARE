# signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Products, notifications
from django.contrib.auth.models import User
from django.dispatch import Signal



#signal for updating mode of payment 
stk_push_success = Signal()






@receiver(post_save, sender=Products)
@receiver(post_delete, sender=Products)
def check_stock_level(sender, instance, **kwargs):
    print(f"Signal triggered for {instance.product_name} with stock level {instance.stock}")
    if instance.stock < instance.alert_quantity:  
        users = User.objects.all()
        for user in users:
            notifications.objects.create(
                user=user,
                Message=f"Product {instance.product_name} stock level is low: {instance.stock} items left."
            )
    else:
         notifications.objects.filter(Message__contains=f"Product {instance.product_name} stock level is low").delete()