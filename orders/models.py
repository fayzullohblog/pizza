from django.db import models
from django.contrib.auth import get_user_model
from .choieces import SizeChoiece,OrderStatus

User=get_user_model()
# Create your models here.

class Order(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    size=models.CharField(max_length=10,default=SizeChoiece.SMALL,choices=SizeChoiece.choices)
    order_status=models.CharField(max_length=10,default=OrderStatus.PENDING,choices=OrderStatus.choices)
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.size} by {self.customer.id} '
    

