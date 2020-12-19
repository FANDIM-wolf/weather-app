
from django.urls import path
from cloud24 import views

urlpatterns = [
    path('',views.home,name='home'),
]