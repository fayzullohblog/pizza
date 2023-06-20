from django.shortcuts import render
from rest_framework import status
from rest_framework  import generics 
from rest_framework import response
from .serializer import UserSerializer
# Create your views here.

class DataGenericApiView(generics.GenericAPIView):
    def get(self,request):
        data={'queryset':'Hellow world'}
        return response.Response(data=data,status=status.HTTP_200_OK)
    
class UserCreateGenericApiView(generics.GenericAPIView):
    
    serializer_class=UserSerializer

    def post(self,request):
        data=request.data
        print('-----',data)
        serializer=self.serializer_class(data=data)
        print('------',serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return response.Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return response.Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    

   