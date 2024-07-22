from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class SignUpForm(UserCreationForm):
    
   
    first_name =forms.CharField(max_length=50, 
      label="", 
      widget=forms.TextInput(attrs={'class': 'form-control',"PlaceHolder":'نام خود را وارد کنید'}))


    last_name =forms.CharField(max_length=50,
      label="",
      widget=forms.TextInput(attrs={'class': 'form-control',"PlaceHolder":'نام خانوادگی  را وارد کنید'}))
    

    
    email =forms.EmailField(max_length=50,
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control',"PlaceHolder":' ایمیل را وارد کنید'}))


    username =forms.CharField(max_length=20,
      label="",
      widget=forms.TextInput(attrs={'class': 'form-control',"PlaceHolder":'نام کاربری  را وارد کنید'}))

    password1 =forms.CharField(label="",widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'name': 'password',
               'type': 'password',
               'placeholder': 'رمز بالای 8 کاراکتر باشد'}))
    

    password2 =forms.CharField(label="",widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'name': 'password',
               'type': 'password',
               'placeholder': 'رمز  را تکرار کنید'}))
    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password1','password2')