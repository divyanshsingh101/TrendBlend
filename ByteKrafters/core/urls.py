from django.urls import path
from core import views
from django.urls import path
from .views import BlogSearchView

app_name="core"
urlpatterns=[
    path('',views.index,name='home'),
    path('login/',views.user_login,name='login'),
    
    path('signup/',views.user_SignUp,name="signup"),
    path('logout/',views.user_logout,name='logout'),
    path('home/',views.home,name="Home"),
    path('cart/',views.cart,name='cart'),
    path('trends/',views.trends,name='trends'),
    path('shipment/',views.shipment,name='shipment'),
    path('login/',views.login,name='login'),
   #  path('index/',views.index,name="home"),
     
     path('reviews/',views.reviews,name='reviews'),
     path('Men/',views.men,name='men'),
     path('women/',views.men,name='women'),
     
    path('search-blogs/', BlogSearchView.as_view(), name='search_blogs'),
    
    
]
