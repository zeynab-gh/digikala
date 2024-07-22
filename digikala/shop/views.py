from django.shortcuts import render,HttpResponse,redirect
from.models import Product,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
from django.http import HttpResponse



def category_summery(request):
      all_cat = Category.objects.all()
      return render(request,'category_summery.html',{'category':all_cat})



def helloworld(request):
    all_products =Product.objects.all()
    return render(request,'index.html',{'products':all_products})

def about(request):
    return render(request,'about.html')

def login_user(request):
    if request.method == "POST":
        username =request.POST['username']
        password=request.POST['password']
        print(username,password)
        

        user=authenticate(request,username=username,password=password)
       
        if user is not None:
            login(request,user)
            messages.success(request,'با موفقیت وارد شدید')
            return redirect('home')
           
        
        else:
            messages.success(request,'نام کاربری یا رمز اشتباه است.دوباره امتحان کنید')
            return redirect("login")

    else:
        
        return render(request,'login.html')


def logout_user(request):
    logout(request)
    messages.success(request,'با موفقیت خارج شدید')
    return redirect('home')



def signup_user(request):
   form=SignUpForm()
   if request.method == 'POST':
       form= SignUpForm(request.POST)
       if form.is_valid(): 
           print(form.is_valid)
           form.save()
           username=form.cleaned_data["username"]
           password1=form.cleaned_data["password1"]
           user=authenticate(request,username=username,password=password1)
           login(request,user)
           messages.success(request,'اکانت شما ساخته شد')
           return redirect("home")
       else:
            messages.success(request,'مشکلی در ثبت نام شما وجود دارد')
            return redirect("signup")
       
   else:
       return render(request,'signup.html',{'form':form})
       
       
def product(request,pk):
    print(pk)
    product = Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})
   
    


def category(request,cat):
    cat=cat.replace("-",'')
    try:
        category = Category.objects.filter(name=cat).first()
        products = Product.objects.filter(Category_id=category.id).all()
        return render(request,'category.html',{'products':products,'category':category})
    except:
        messages.success(request,('دسته بندی وجود ندارد'))
        return redirect("home")
                    
    


