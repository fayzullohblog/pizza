from django.shortcuts import render
from rest_framework import status
from rest_framework import generics 
from rest_framework import response 
from rest_framework.permissions import IsAdminUser

from .models import Order
from .serializer import OrderSerializer
# Create your views here.

class OrderGenericApiView(generics.GenericAPIView):
    def get(self,request):
        data={'queryset':'Hellow Order'}
        return response.Response(data=data,status=status.HTTP_200_OK)
        

class OrderCreateListGenericsApiView(generics.GenericAPIView):
    serializer_class=OrderSerializer
    queryset=Order.objects.all()
    permission_classes=[IsAdminUser]
    
    def get(self,request):
        serializer=self.serializer_class(instance=Order.objects.all(),many=True)
        return response.Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        user=request.user
        if serializer.is_valid():
            serializer.save(customer=user)
            return response.Response(data=serializer.data,status=status.HTTP_200_OK)
        return response.Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
class OrderCreateListDetailGenericsApiView(generics.GenericAPIView):
    serializer_class=OrderSerializer
    queryset=Order.objects.all()

    def get(self,request,pk):
        queryset=self.queryset.get(id=pk)
        serializer=self.serializer_class(queryset)
        return response.Response(data=serializer.data)
        


        


