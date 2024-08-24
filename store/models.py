from itertools import product
from pyexpat import model
from random import choices
from re import L
from django.db import models
from django.forms import IntegerField

from store.views import category
# Create your models here.
class User (models.Model) :
    UserID = models.IntegerField(primary_key= True) 
    UserName = models.CharField(max_length=50) 
    password = models.CharField(max_length=50)
    Email = models.EmailField()
    role = models.CharField(max_length=50) 
class Complaint(models.Model) :
    ComplaintId = models.IntegerField(primary_key= True)
    ComplaintDate= models.DateTimeField()
    UserID = models.ForeignKey( User , on_delete=models.CASCADE) 
    ComplaintText = models.IntegerField()
    Status = models.CharField(max_length=50)
class Store(models.Model):
    StoreID = models.IntegerField(primary_key=True)
    StoreName = models.CharField(max_length=50)
    OwnerName = models.CharField(max_length=50)
    StoreOwner = models.CharField(max_length=50)
    PassWord = models.CharField(max_length=50)
    Email = models.EmailField()
    Verifications = models.FileField(blank=True, null=True) 
    logo = models.FileField(blank=True, null=True) 
    Category = models.CharField(max_length=50,null =True)
    def __str__ (self) :
        return f"{self.StoreName} ({self.Category})"
class Order (models.Model) :
    OrderID = models.IntegerField(primary_key=True)
    OrderDate = models.DateTimeField(auto_now=True)
    UserID = models.ForeignKey( User , on_delete=models.CASCADE)
    StoreId = models.ForeignKey(Store, on_delete= models.CASCADE) 
    OrderStatus = models.CharField(max_length=5)
class Product (models.Model) : 
    ProductID = models.IntegerField(primary_key=True) 
    productName = models.CharField( max_length=50) 
    productDescription = models.CharField(max_length=500) 
    Price = models.IntegerField()
    StockQuantity = models.CharField( max_length=50 )
    StoreID = models.ForeignKey(Store , on_delete= models.CASCADE)
class OrderItem (models.Model) : 
    OrderItemID = models.IntegerField(primary_key=True) 
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE) 
    ProductID = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
class Rating(models.Model):
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'), 
    ]
    RatingID = models.CharField(choices= RATING_CHOICES,max_length=200 , primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE)    
    ReviewgText = models.TextField(max_length= 500, null=True, blank=True)
class Favorite(models.Model) :
    FavoriteID =models.IntegerField(primary_key=True) 
    UserID = models.ForeignKey(User,on_delete= models.CASCADE )
    ProductID = models.ForeignKey(Product,on_delete= models.CASCADE)