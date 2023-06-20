from django.urls import path 
from .views import OrderGenericApiView

urlpatterns = [
    path('',OrderGenericApiView.as_view())
]