from django.urls import path
from . import views 

urlpatterns = [
   path('',views.home ,name ='home') ,
   path('Category/',views.category , name='category') , 
   path('Category/Store/',views.store,name='store') , 
   #path('Home/Cart/', views.cart , name= 'cart') ,
   path('/signup/', views.signup,name= 'signup') , 
   path('/Login/',views.login,name='login') ,
   path('admin/',views.admin , name= 'admin') , 
   path('CreateStore', views.create_store , name= 'create_store')
]