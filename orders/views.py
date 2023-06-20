from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
# Create your views here.

class OrderGenericApiView(GenericAPIView):
    def get(self,request):
        data={'queryset':'Hellow Order'}
        return Response(data=data,status=status.HTTP_200_OK)
        
    

