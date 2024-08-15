from django import forms
from .models import User, Order , Favorite ,Complaint ,Rating ,Store
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
class ComplaintForm(forms.ModelForm) : 
    class Meta : 
        model = Complaint 
        fields = ['ComplaintId' , 'ComplaintDate', 'userID' ,'ComplaintText' ,
                  'Status'] 
class SignUpForm(UserCreationForm): 
    class Meta : 
        model = User 
        fields = ['username' , 'password', 'email']
class JoinStore(forms.Form) : 
    class Meta : 
        model = Store 
        fields = '__all__'
class MakeOrder(forms.ModelForm)  : 
    class Meta : 
        model : Order 
        fields = ['StoreId' ,'UserID','TotalAmount'] 
class MakeFavorite (forms.ModelForm) : 
    class Meta :
        model : Favorite 
        fields = '__all__'
class MakeRate (forms.Form) : 
    class Meta : 
        model : Rating 
        fields = '__all__'