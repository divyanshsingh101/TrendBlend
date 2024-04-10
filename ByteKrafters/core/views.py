from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request,'core/home.html')

def cart(request):
  return render(request,'core/cart.html')
 
def trends(request):
  return render(request,'core/trends.html')

def shipment(request):
  return render(request,'core/shipment.html')