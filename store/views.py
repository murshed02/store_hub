from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib import messages
from .models import OrderItem ,Product ,User 
from .forms import User ,Login , Signup
def home(request) : 
    from store.models import Store
    categories = Store.objects.values_list('Category', flat=True).distinct()
    context = {
        'categories': categories
    }
    return render(request, 'Home/Category.html', context)
def category (request) : 
    from store.models import Store
    stores = Store.objects.filter(Category=category)
    return render (request,'catergory.html',{stores: stores, 'category' : category})
def store(request, store_id):
    products = Product.objects.filter(StoreID=store_id)
    return render(request, 'store_products.html', {'products': products})
def cart (request) : 
    from store.models import OrderItem 
    cart = OrderItem.objects.all() 
    return render (request,'Home/Cart',cart) 
def admin (request) : 
    pass 
def Store_admin (request) : 
    pass 
def create_store (request) :
    from store.models import Store 
    store = Store.objects.all()
    return render (request , 'Home/CreateStore', store) 
def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = User.objects.filter(username=username, password=password).first()
            if user: 

                
                messages.success(request, "Login successful!")
                return redirect('home')  
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = Login()
    return render(request, 'login.html', {'form': form}) 


def signup(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Signup successful!")

            return redirect('login')  # Redirect to login page after signup
    else:
        form = Signup()
    return render(request, 'signup.html', {'form': form})