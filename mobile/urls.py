from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add-mobile/',views.add_mobile,name='add_mobile'),
    ]