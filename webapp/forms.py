from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import EmailInput,PasswordInput,TextInput
from django import forms
from .models import Record
class RegisterUser(UserCreationForm):
    
    
    class Meta:
        
        model = User
        fields = ['username']
        
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
    
class CreateRecordForm(forms.ModelForm):
    
    class Meta:
        model = Record
        fields = ['first_name','last_name','email','phone','city','address','provinace','country']
        

class UpdateRecordForm(forms.ModelForm):
        
    class Meta:
        model = Record
        fields = ['first_name','last_name','email','phone','city','address','provinace','country']