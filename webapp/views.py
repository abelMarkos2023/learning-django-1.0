from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from .forms import RegisterUser,LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    # return HttpResponse('Hello World')
    return render(request, 'webapp/index.html')

def register(request):
    
    form = RegisterUser
    
    if request.method == 'POST' :
        
        form = RegisterUser(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {'form' : form}
    
    return render(request,'webapp/register.html',context)

def loginView(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request,username=username,password=password)
            
            if user is not None :
                login(request, user)
                print(user)
                return redirect('dashboard')
        
    context = {'form' : form}
    
    return render(request,'webapp/login.html',context)


@login_required(login_url='login')
def dashboard(request):
    
    return render(request,'webapp/dashboard.html')

def logout(request):
    auth.logout(request)
    return redirect('home')