from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here. 
''' to not create a login user this way is enough

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
''' 
def home(request) : 
    pass 
def category (request) : 
    pass 
def store (request) : 
    pass 
def cart (request) : 
    pass 
def signin (request) : 
    pass
def login (request) : 
    pass 
def admin (request) : 
    pass 
def create_store (request) : 
    pass