from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here. 
from django.shortcuts import render, redirect
from .models import OrderItem ,Product
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