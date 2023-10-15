from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from .models import User
import os
from django.conf import settings


# Create your views here.
def func():
    print('Hello')

def login(request):
    if request.method=='POST':
        uname = request.POST['username']
        passw = request.POST['password']
        user = User.objects.get(username=uname)

        password_matches = check_password(passw, user.password)
        if password_matches:
            return redirect('/home/')

    return render(request,'catalyst_user/login.html',{})

def home(request):
    return render(request,'catalyst_user/home.html',{})

def upload(request):
    if request.method=='POST':
        file = request.FILES['file']
        folder_path = 'catalyst_user/static/uploaded_file/'
        with open(folder_path+file.name,'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
                print('success')
    
    return render(request,'catalyst_user/upload.html',{})

def user_form(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        passw = request.POST['password']
        hashed_passw = make_password(passw)
        User.objects.create(
            username = uname,
            email = email,
            password = hashed_passw
        )
        return redirect('/user-add/')
    return render(request,'catalyst_user/user_form.html',{})

def query(request):
    return render(request,'catalyst_user/query.html',{})


def user_add(request):
    all_user = User.objects.all()
    return render(request,'catalyst_user/user.html',{'users':all_user})


def logout(request):
    return redirect('/login/')

