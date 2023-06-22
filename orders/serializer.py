from rest_framework import serializers
from .models import Order
from .choieces import SizeChoiece,OrderStatus

class OrderSerializer(serializers.ModelSerializer):
    quantity=serializers.IntegerField()
    size=serializers.ChoiceField(choices=SizeChoiece.choices)
    order_status=serializers.ChoiceField(choices=OrderStatus.choices)

    class Meta:
        model=Order
        fields=['quantity','size','order_status']

