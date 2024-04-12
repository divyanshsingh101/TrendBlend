from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from django.views.generic import ListView,DetailView
from core.models import Blog
from django.shortcuts import redirect

# Create your views here.
def home(request):
  return render(request,'core/home.html')

def cart(request):
  return render(request,'core/cart.html')
 
def trends(request):
  return render(request,'core/trends.html')

def shipment(request):
  return render(request,'core/shipment.html')
def reviews(request):
  return render(request,'core/review.html')
  def men(request):
  allmen=Product.objects.filter(title='MALE')
  context={'men_category':allmen}
  return render(request,'core/Men.html',context)

def women(request):
  all_women=Product.objects.filter(title='WOMEN')
  context_={'women_category':all_women}
  return render(request,'core/women.html',context_)


def index(request):
  return render(request,'core/registration/index.html')

def user_SignUp(request):
  if request.method=='POST':
    form=SignupForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/login')
  else:
    form=SignupForm()
  return render(request,'core/registration/signup.html',context={'form': form})
 
def user_login(request):
  if request.method=='POST':
    form=LoginForm(request.POST)
    if form.is_valid():
      username=form.cleaned_data['username']
      password=form.cleaned_data['password']
      user=authenticate(request,username=username,password=password)
      if user:
        login(request,user)
        return redirect('/home')
  else:
    form=LoginForm()
  return render(request,'core/registration/login.html',{'form':form})

def user_logout(request):
  logout(request)
  return redirect('/login')

class BlogSearchView(ListView):
  model=Blog
  template_name='home.html'
  context_object_name='posts'

  def get_queryset(self):
    query=self.request.GET.get('q')
    return Blog.objects.filter(title__icontains=query).order_by('-created_at')


def search_view(request):
  query=request.GET.get("q")
