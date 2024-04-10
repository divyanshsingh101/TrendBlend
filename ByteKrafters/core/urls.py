from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name="home"),
    path('home/',views.home,name="home"),
    path('cart/',views.cart,name='cart'),
    path('trends/',views.trends,name='trends'),
    path('shipment/',views.shipment,name='shipment'),
    
]