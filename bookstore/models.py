from django.db import models
from django.contrib.auth.models import User

class Costumer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=190,null=True) 
    email=models.CharField(max_length=190, null=True)
    phone=models.CharField(max_length=190, null=True)
    age  =models.CharField(max_length=190, null=True)
    date =models.DateTimeField(auto_now_add=True, null=True)
    avater =models.ImageField(blank=True,null=True)
# Create your models here.
    def __str__(self):
       return self.name
    
class Tag(models.Model):
    name=models.CharField(max_length=190,null=True)
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    CATEGORY=(
        ('Classics','Classics'),
        ('Comic book','Comic book'),
        ('Ranaf','Ranaf'),
        ('Zeeedmil','Zeeedmil')
    )
    name = models.CharField(max_length=190, null=True)
    auther=models.CharField(max_length=190,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=190,null=True,choices=CATEGORY)
    descrption=models.CharField(max_length=190,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    tages=models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

class Order(models.Model):

    STATUS={
        ('Peding','Peding'),
        ('Delivred','Delivred'),
        ('in progress','in progress'),
        ('out of order','out of order')
    }
    costumer= models.ForeignKey(Costumer,null=True,on_delete=models.SET_NULL)
    book=models.ForeignKey(Book,null=True,on_delete=models.SET_NULL)
    tages=models.ManyToManyField(Tag)
    Date_created=models.DateTimeField(auto_now_add=True,null=True)
    stauts=models.CharField(max_length=190,null=True,choices=STATUS)
    