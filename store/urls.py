from django.urls import path
from . import views

urlpatterns = [
   path('Home/',views.home ,name ='home') ,
   path('Home/Category/',views.category , name='category') , 
   path('Home/Category/Store/',views.store,name='store') , 
   path('Home/Cart/', views.cart , name= 'cart') ,
   path('Home/Signin/', views.signin,name= 'signin') , 
   path('Home/Login/',views.login,name='login') ,
   path('Home/admin/',views.admin , name= 'admin') , 
   path('Home/CreateStore', views.create_store , name= 'create_store')
]