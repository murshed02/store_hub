from dataclasses import fields
from multiprocessing import AuthenticationError
from django import forms
from .models import User, Order  ,Complaint ,Rating ,Store 
from django.contrib.auth.models import User 
class ComplaintForm(forms.ModelForm) : 
    class Meta : 
        model = Complaint 
        fields = ['ComplaintId' , 'ComplaintDate', 'UserID' ,'ComplaintText' ,
                  'Status'] 
class JoinStore(forms.Form) : 
    class Meta : 
        model = Store 
        fields = '__all__'
class MakeOrder(forms.ModelForm)  : 
    class Meta : 
        model : Order 
        fields = ['StoreId' ,'UserID','TotalAmount'] 
# class MakeFavorite (forms.ModelForm) : 
#     class Meta :
#         model : Favorite 
#         fields = '__all__'
class MakeRate (forms.Form) : 
    class Meta : 
        model : Rating 
        fields = '__all__'
from django import forms

class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput()) 

class Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password'] 
class Registration_request(forms.ModelForm) : 
    class Meta : 
        model = Store 
        fields= ['StoreName' , 'OwnerName', 'Email'  ,'PassWord' 
                 ,'Verifications' ,'logo' ,'Category']