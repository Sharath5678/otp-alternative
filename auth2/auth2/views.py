from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from codes.forms import CodeForm
from users.models import CustomUser
from codes.models import Product
from .utils import send_sms 
from django.contrib.auth.models import User
from django.contrib import messages


def home_view(request):
    return render (request, 'main.html',{})

def auth_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user is not None:
            request.session['pk']=user.pk
            return redirect('verify-view')
    return render(request, 'auth.html',{'form':form})


def verify_view(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    if(pk):
        user = CustomUser.objects.get(pk=pk)
        code= user.code 
        code_user = f"{user.username}:{user.code}"
        if not request.POST:
            print(code_user)
            send_sms(code_user, user.phone_number)
        if form.is_valid():
            num = form.cleaned_data.get('number')
            
            if str(code)==num:
                code.save()
                login(request,user)
                return redirect('home-view')
            else:
                return redirect('login-view')
            
    return render(request, 'verify.html', {'form':form})


def register_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        phone_number=request.POST['phone_number']
        if CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'username is taken')
                return redirect('register-view')
        else:
                    user = CustomUser.objects.create_user(username=username, phone_number = phone_number, password=password)

                    user.save();                
                    return redirect('login-view')        
    return render(request,'register.html') 

def logout_view(request):
    logout(request)
    return redirect('/')

def ProductList(request):
    if request.user.is_authenticated:
            
            prod = Product.objects.all
            return render(request, 'ProductList.html',{'prod': prod})
    else:
            return redirect('login-view')

def order(request,productname):
    p=Product.objects.get(Name=productname)
    context={'p':p}
    return render(request,'order.html',context)

def about(request):
    return render(request,'AboutUs.html')
            