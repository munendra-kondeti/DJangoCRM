from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout;
from django.contrib import messages;
from .forms import SignupForm,AddForm
from .models import Record
# Create your views here.

def home(request):
    records = Record.objects.all();
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
        return render(request,'home.html',{'records':records});

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
    
def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk);
        return render(request,'record.html',{'record':customer_record});
    else:
        messages.error(request,"Login first");
        return redirect('home');
   
def delete_record(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk);
        customer_record.delete();
        messages.success(request,"Delete successfully");
        return redirect('home');
    else:
        messages.error(request,"Login first");
        return redirect('home'); 

def add_record(request):
    addForm = AddForm(request.POST or None);
    if request.user.is_authenticated:
        if request.method == 'POST':
            if addForm.is_valid():
                addForm.save();
                messages.success(request,"Add successfully");
                return redirect('home');
            
        return render(request,'add_record.html',{'form':addForm});
    else:
        messages.error(request,"Login first");
        return redirect('home');