from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here. 
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .forms import SignUpForm, CustomAuthenticationForm
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
def home(request) : 
    from store.models import Store
    stores = Store.objects.values("StoreName","logo","Category")
    return render(request, 'store/home.html', {'stores':stores} ) 
def category (request) : 
    from store.models import Store
    categories = Store.objects.values_list('Category', flat=True).distinct()
    context = {
        'categories': categories
    }
    return render(request, 'Home/Category.html', context)
def store (request) : 
    pass 
#هي الا لزمة ولا لان اذا موجودة في الهوم فخلص بكفي 
def cart (request) : 
    from store.models import OrderItem 
    cart = OrderItem.objects.all() 
    return render (request,'Home/Cart',cart) 
def signin (request) :  
    pass
def login (request) : 
    pass 
def admin (request) : 
    pass 
def create_store (request) :
    from store.models import Store 
    store = Store.objects.all()
    return render (request , 'Home/CreateStore', store) 