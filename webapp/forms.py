from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import EmailInput,PasswordInput,TextInput
from django import forms

class RegisterUser(UserCreationForm):
    
    
    class Meta:
        
        model = User
        fields = ['username']
        
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    