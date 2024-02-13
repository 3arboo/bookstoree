from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as Authviews

urlpatterns = [
    path('',views.home,name= 'home'),
    path('books/',views.books ,name= 'books'),
    path('costumer/<str:pk>',views.customer ,name= 'customer'),
    path('create/<str:pk>',views.create ,name= 'create'),
    path('update/<str:pk>',views.update ,name= 'update'),
    path('delete/<str:pk>',views.delete ,name= 'delete'),
    path('register/', views.register , name= 'register'),
    path('login/',views.userlogin ,name= 'login'),
    path('logout/',views.userlogout ,name= 'logout'),
    path('profile/',views.userProfile ,name= 'profile'),
    path('profile_info/',views.Profileinfo ,name= 'Pro_info'),


    path('reset_password/',Authviews.PasswordResetView.as_view(template_name="bookstore/password_reset.html") ,name= 'reste_password'),
    path('reset_password_sent/',Authviews.PasswordResetDoneView.as_view(template_name="bookstore/password_reset_sent.html") ,name= 'password_reset_done'),
    path('reset/<uidb64>/<token>/',Authviews.PasswordResetConfirmView.as_view(template_name="bookstore/password_reset_form.html"),name= 'password_reset_form'),
    path('reset_password_complete/',Authviews.PasswordResetCompleteView.as_view(template_name="bookstore/password_reset_done.html") ,name= 'password_reset_sent'),
    
]
