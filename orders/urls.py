from django.urls import path 
from . import views

urlpatterns = [
    path('',views.OrderGenericApiView.as_view()),
    path('create-list/',views.OrderCreateListGenericsApiView.as_view()),
    

]
