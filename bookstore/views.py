from django.shortcuts import render,redirect
from django.http import HttpResponse
from bookstore.models import *
from .froms import OrderForms,CreateNewUser
from .filters import OrderFilters 
from django.contrib import messages
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .decorators import notLoggedUsers , allowedUsers , ForAdmin
from django.contrib.auth.models import Group
import requests
from django.conf import settings
@login_required(login_url='login')
@allowedUsers(allowedGroups='admin')
def home(request):
    costumer=Costumer.objects.all()
    order =Order.objects.all()
    t_order= order.count()
    p_order = order.filter(stauts='Peding').count()
    d_order = order.filter(stauts='Delivred').count()
    in_order = order.filter(stauts='in progress').count()
    out_order = order.filter(stauts='out of order').count()
    context = {'costumer':costumer,
               'order':order,
               't_order':t_order,
               'p_order':p_order,
               'd_order':d_order,
               'in_order':in_order,
               'out_order':out_order,}
    return render(request , 'bookstore/dashboard.html',context)


@login_required(login_url='login')
@ForAdmin
def books(request):
    books= Book.objects.all()
    return render(request ,'bookstore/books.html',{'books':books})

@login_required(login_url='login')
@ForAdmin
def customer(request,pk):
    costumer = Costumer.objects.get(id=pk)
    order = costumer.order_set.all()
    N_order = order.count()
    searchfilter = OrderFilters(request.GET ,queryset=order)
    order = searchfilter.qs
    context = {'costumer':costumer,'searchfilter':searchfilter,
               'order':order, 'N_order':N_order}
    return render(request , 'bookstore/costumer.html',context)


'''def create(request):
    order = Order.objects.all()
    form = OrderForms()
    if request.method == 'POST':
        print(request.POST)
        form = OrderForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}    
    return render(request ,'bookstore/My_order_form.html', context)'''
@login_required(login_url='login')
@ForAdmin
def create(request,pk):
    OrderFormSet = inlineformset_factory(Costumer,Order,fields=('book','stauts'),extra=8)
    costumer = Costumer.objects.get(id=pk)
    formset = OrderFormSet(queryset= Order.objects.none(),instance= costumer)
    if request.method == 'POST':
        print(request.POST)
        formset = OrderFormSet(request.POST,instance=costumer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}    
    return render(request ,'bookstore/My_order_form.html', context)

@login_required(login_url='login')
@allowedUsers(allowedGroups='costumer')
def update(request,pk):
    order =Order.objects.get(id=pk)
    formset = OrderForms(instance=order)
    if request.method == 'POST':
        formset = OrderForms(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset,'order':order}    
    return render(request ,'bookstore/My_order_form.html', context)

@login_required(login_url='login')
@ForAdmin
def delete(request,pk):
    order =Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'order':order}    
    return render(request ,'bookstore/delete_forms.html', context)


def register(request):
        form = CreateNewUser()
        if request.method == 'POST':
            form = CreateNewUser(request.POST)
            if form.is_valid() :
                racaptcha_response=request.POST.get('g-recaptcha-response')
                data={
                    'secret':settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response': racaptcha_response
                }
                r=requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
                resultat=r.json()
                if resultat['success']:
                    user =form.save()
                    username = form.cleaned_data.get('username')
                    group = Group.objects.get(name='costumer')
                    user.groups.add(group)
                    messages.success(request  ,username + 'Created Successfuly...!')
                    return redirect('login')
                else:
                    messages.error(request,'invalid Recaptcha Please try again !!')
        context = {'form':form}    
        return render(request ,'bookstore/register.html', context)

@notLoggedUsers
def userlogin(request):

        if request.method== 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password1')
            print(request.POST.get('username'))
            print(request.POST.get('password1'))
            user = authenticate(request, username= username , password = password)
            if user is not None:
                login(request,user)
                return redirect('profile')
            else:
                messages.info(request,'verifier username ou password')
        
        return render(request ,'bookstore/login.html')

def userlogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowedUsers(allowedGroups='costumer')
def userProfile(request):
    order = request.user.costumer.order_set.all()
    t_order= order.count()
    p_order = order.filter(stauts='Peding').count()
    d_order = order.filter(stauts='Delivred').count()
    in_order = order.filter(stauts='in progress').count()
    out_order = order.filter(stauts='out of order').count()
    context = {
               'order':order,
               't_order':t_order,
               'p_order':p_order,
               'd_order':d_order,
               'in_order':in_order,
               'out_order':out_order,}
    return render(request ,'bookstore/profile.html', context)


@login_required(login_url='login')
@allowedUsers(allowedGroups='costumer')
def Profileinfo(request):
   
    context = {}
    return render(request ,'bookstore/profile_info.html', context)
# Create your views here.
