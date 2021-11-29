from django.shortcuts import render , redirect
from django.contrib.auth.models import User,auth

import accounts
from .models import Profile
from . forms import Login_Form , UserCreationForm 
from django.contrib.auth import authenticate, login
from django.contrib import messages  
from django.contrib.auth.decorators import login_required

# Create your views here.



def index(request):
    doctors = Profile.objects.all()
    context = {
        'doctors' : doctors
    }
    return render(request,'index.html',context)


def doctor_profile(request,slug):   
    doctor_profile = Profile.objects.get(slug=slug)
    context = { 
        'doctor_profile' : doctor_profile
    }
    return render(request,'doctor_profile.html',context) 

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)      # Check Authentication
        if user is not None:        # يعني لو اليوزر موجود
            auth.login(request,user)
            return redirect ('/')  # Redirect to a success 
    else:
        form = Login_Form()
    context = {
        'form' : form
    }
    return render(request,'login.html',context)
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            login(request , user)
            return redirect('/')
    else:
        form = UserCreationForm()
        
    return render(request,'singnup.html',{'form':form})



    
@login_required(login_url='accounts:login')
def my_profile(request):
    return render(request,'myprofile.html')

