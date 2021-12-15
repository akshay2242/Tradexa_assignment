from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User as Ur
from django.forms import fields, widgets
from .models import Post,User
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = Ur
        fields = ['username','first_name', 'last_name','email']
        labels = {'first_name':'First Name', 'last_name':'Last Name', 'email':'Email'}
        widgets = {'username':forms.TextInput,
                 'first_name':forms.TextInput,
                 'last_name':forms.TextInput,
                 'email':forms.EmailInput
                  }
        
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'