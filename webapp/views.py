from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegisterUser,LoginForm

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
            return redirect('home')
        
    context = {'form' : form}
    
    return render(request,'webapp/register.html',context)

def login(request):
    form = LoginForm
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form' : form}
    
    return render(request,'webapp/login.html',context)