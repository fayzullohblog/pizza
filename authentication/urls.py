from django.urls import path
from . import views

urlpatterns = [
    path('hell/',views.DataGenericApiView.as_view(),name='datagenricapiview'),
    path('user-data/',views.UserCreateGenericApiView.as_view(),name='usercreategeneric'),
]