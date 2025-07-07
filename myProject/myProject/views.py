from django.shortcuts import render, redirect
from myApp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def signupPage(request):
    
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        user_type = request.POST.get("user_type")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        contact_no = request.POST.get("contact_no")
        
        
        if password == confirm_password:
            
            user = customeUser.objects.create_user(
                username = username,
                email = email,
                password = password,
                user_type= user_type,
                gender = gender,
                age = age,
                contact_no = contact_no
            )
            return redirect("signinPage")
    
    
    return render(request, "signupPage.html")



def signinPage(request):
    
    if request.method == 'POST':
        user_name = request.POST.get("username")
        pass_word = request.POST.get("password")
        
        try:
            user = authenticate(request, username=user_name, password = pass_word)
            
            if user is not None:
                login(request, user)
                return redirect("homePage")
            else:
                return redirect("signinPage")
        
        except customeUser.DoesNotExist:
            return redirect("homePage")
            
            
    return render(request, "signinPage.html")


@login_required
def homePage(request):
    
    
    return render(request, "homepage.html")


def logoutPage(request):
    
    logout(request)
    
    return render(request, "signinPage.html")