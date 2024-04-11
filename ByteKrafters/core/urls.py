from django.urls import path
from core import views
app_name="core"
urlpatterns=[
    path('',views.home,name="home"),
    path('home/',views.home,name="home"),
    path('cart/',views.cart,name='cart'),
    path('trends/',views.trends,name='trends'),
    path('shipment/',views.shipment,name='shipment'),
   #  path('index/',views.index,name="home"),
    
]