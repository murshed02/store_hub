from multiprocessing import AuthenticationError
from django import forms
from .models import User, Order , Favorite ,Complaint ,Rating ,Store ,Profile
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
class ComplaintForm(forms.ModelForm) : 
    class Meta : 
        model = Complaint 
        fields = ['ComplaintId' , 'ComplaintDate', 'userID' ,'ComplaintText' ,
                  'Status'] 
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    location = forms.CharField(max_length=30, required=False)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'location', 'birth_date')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user.profile.location = self.cleaned_data['location']
            user.profile.birth_date = self.cleaned_data['birth_date']
            user.profile.save()
        return user
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
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