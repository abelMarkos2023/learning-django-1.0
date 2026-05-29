from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from .forms import RegisterUser,LoginForm,CreateRecordForm,UpdateRecordForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages


from .models import Record

# Create your views here.

def home(request):
    # return HttpResponse('Hello World')
    return render(request, 'webapp/index.html')

def register(request):
    
    form = RegisterUser()
    
    if request.method == 'POST' :
        
        form = RegisterUser(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully")
            return redirect('login')
        
    context = {'form' : form}
    
    return render(request,'webapp/register.html',context)

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
        
    context = {'form' : form}
    
    return render(request,'webapp/login.html',context)


@login_required(login_url='login')
def dashboard(request):
    
    my_records = Record.objects.all()
    
    context = {'my_records' : my_records}
    
    return render(request,'webapp/dashboard.html',context)


@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(request,"Record created successfully")
            
            return redirect('/dashboard')
    context = {'form':form}
    return render(request,'webapp/create-record.html',context)

@login_required(login_url='login')
def update_record(request,pk):
    
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST,instance=record)
        
        if form.is_valid():
            form.save()
            
            messages.success(request,"record Updated Successfully")
            
            return redirect('/dashboard')
    context = {'form':form}
    return render(request,'webapp/update-record.html',context)



@login_required(login_url='login')

def delete_record(request,pk):
    
    record = Record.object.get(id=pk)
    
    record.delete()
    
    return redirect('dashboard')


@login_required(login_url='login')
def view_record(request,pk):
    
    record = Record.objects.get(id=pk)


    context = {'record':record}
    return render(request,'webapp/view-record.html',context)
def logout(request):
    auth_logout(request)
    return redirect('home')