from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout;
from django.contrib import messages;
from .forms import SignupForm
# Create your views here.

def home(request):
    # check to see if the user is logged in
    if request.method == 'POST':
        userName = request.POST.get('userName'); 
        password = request.POST['pwd'];
        user = authenticate(request,username=userName,password= password);
        
        if user is not None:
            login(request,user);
            messages.success(request,"You login successfully");
            return redirect('home');
        else:
            messages.error(request,"Invalid username or password");
            return redirect('home');
    else:
        return render(request,'home.html',{});

def login_user(request):
    return render(request,'login.html',{});

def logout_user(request):
    logout(request);
    messages.success(request,"You logout successfully");
    return redirect('home');

def register_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST);
        if form.is_valid():
            form.save();
            username = form.cleaned_data['username'];
            password = form.cleaned_data['password1'];
            user = authenticate(username=username,password= password);
            login(request,user);
            messages.success(request,"You register successfully");
            return redirect('home');
    else:
        form = SignupForm();
        return render(request,'register.html',{'form':form});