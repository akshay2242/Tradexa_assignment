from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib.auth import authenticate, login, logout
from .models import Post,User
from django.contrib.auth.models import User as Ur
# Home
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})


# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# Signup
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['first_name']
            lm = form.cleaned_data['last_name']
            em = form.cleaned_data['email']
            us = form.cleaned_data['username']
            ps = form.cleaned_data['password1']
            form1 = User(first_name=nm,last_name=lm,email=em,username=us,password=ps) 
            user = form.save()
            form1.save()  
            form = SignUpForm()   
            return HttpResponseRedirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

# Login
def user_login(request):
    if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:    
                    login(request,user)
                    return HttpResponseRedirect('/dashboard/')

    else:        
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

def dashboard(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            form = PostForm()
    else:
        form = PostForm()
    return render(request,'dashboard.html', {'form':form})
