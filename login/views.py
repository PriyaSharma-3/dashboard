from django.shortcuts import render,redirect
from .forms import LoginForm  
from .models import Login  
from django.contrib import messages
from django.contrib.auth import authenticate, login


def login(request):
    # if request.method == "POST":  
    #     form = LoginForm(request.POST)  
    #     if form.is_valid():  
    #         try:  
    #             form.save()  
    #             return redirect('/index')  
    #         except:  
    #             pass  
    # else:  
    #     form = LoginForm()  
    # return render(request,'login.html',{'form':form})   


    if request.method == 'POST':
        form = LoginForm(request.POST)  
        username = request.POST['username']
        password = request.POST['password']
         
        try:
            login = Login.objects.get(username = username,password=password)   
           
        except Login.DoesNotExist:
            login = None
            messages.error(request, "Invalid username or password")

        if login is not None:
            return redirect('/consumer')                                           
        else:
            return render(request, 'login.html')

    return render(request,'login.html')
