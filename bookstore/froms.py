from django.forms import ModelForm
from .models import Order ,Costumer
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class OrderForms(ModelForm):
    class Meta:
        model = Order
        fields= '__all__'

class CostumerForm(ModelForm):
    class Meta:
        model = Costumer
        feilds = "__all__"
        exclude={'book','stauts'}

class CreateNewUser(UserCreationForm):
    class Meta:
        model= User
        fields={'username','email','password1','password2'}
        