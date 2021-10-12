from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login,logout


def signin(request ):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('homepage')
    else:
        form=AuthenticationForm()
    
    return render(request,'adduser.html',{'form':form})
