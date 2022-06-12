from pdb import post_mortem
from django.contrib import messages,auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.forms import modelform_factory
from .models import blog
# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password, 
                                        email=email, first_name=first_name, last_name=last_name)
                user.save()
                
                return redirect('login_user')


        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
            

    else:
        return render(request, 'registeration.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')



    else:
        return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def logout_user(request):
    auth.logout(request)
    return redirect('login_user')


NewArticle = modelform_factory(blog,exclude=[])


def addarticle(request):
    if request.method== 'POST':
        form=NewArticle(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            print("form not valid")
    else:
        return render(request, 'addarticle.html')

