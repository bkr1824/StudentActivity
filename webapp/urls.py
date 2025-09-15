"""WebC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [ 


    path('', views.homepage, name="WelcomeHome"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminloginaction/', views.adminloginaction, name="adminloginaction"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('userhome/', views.userhome, name="userhome"),
    
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('usignupaction/', views.usignupaction, name="usignupaction"),
    path('user/', views.user, name="user"),
    path('forgotpwd/', views.forgotpwd, name="forgotpwd"),

    
    path('signup/', views.signup, name="signup"),
    path('userloginaction/', views.userloginaction, name="userloginaction"),
    
    path('userlogout/', views.userlogout, name="userlogout"),
    path('profile/', views.viewprofilepage, name="viewprofile"),
    path('updateprofile/', views.updateprofile, name="updateprofile"),

    
    
    path('addfaculty/', views.addfaculty, name="addfaculty"),
    path('viewfaculty/', views.viewfaculty, name="viewfaculty"),
    path('updatepwd/', views.updatepwd, name="updatepwd"),

    path('pplsearch/', views.pplsearch, name="pplsearch"),
    path('addbooks/', views.addbooks, name="addbooks"),
    path('addevents/', views.addevent, name="addevent"),

    path('addlib/', views.addlib, name="addlib"),
    path('addbook/', views.addbook, name="addbook"),
    path('booksearch/', views.booksearch, name="booksearch"),
    path('purchasebooks/', views.purchasebooks, name="purchasebooks"),
    path('payment_u/', views.payment_u, name="payment_u"),
    path('roommate/', views.roomreqstore, name="roomreqstore"),
    path('searchroommate/', views.searchroommate, name="searchroommate"),
    path('mealplan/', views.mealplandef, name="mealplan"),

    path('getevents/', views.getevents, name="getevents"),
    path('bookevent/', views.bookeventsdef, name="bookevent"),
    path('bookbus/', views.bookbus, name="bookbus"),
    path('bookbusaction/', views.bookbusaction, name="bookbusaction"),
    
    path('bookbusaction2/', views.bookbusaction2, name="bookbusaction2"),
    
    path('regvoting/', views.regvoting, name="regvoting"),
    path('addvotes/', views.addvotes, name="addvotes"),
    
    
    


    
    
   
]
