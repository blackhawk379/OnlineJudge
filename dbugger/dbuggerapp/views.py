import time

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from dbugger.models import problems


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['signUpUser']
        print('HERE', username)
        email = request.POST['signUpEmail']
        password = request.POST['signUpPass']
        rPassword = request.POST['signUpRPass']
        if rPassword == password:
            x = User.objects.create_user(username=username, password=password, email=email)
            x.save()
            messages.success(request, "Account Created Successfully!!")
            time.sleep(2)
            return render(request, 'home.html')
        else:
            messages.error(request, "Passwords Don't Match!!")
            time.sleep(2)
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')


def signin(request):
    if request.user.is_authenticated:
        render(request, 'second.html')
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, "Login Successful")
            time.sleep(2)
            problem = problems.objects.all()
            return render(request, 'second.html', {'problem': problem})
        else:
            messages.error(request, "Incorrect Username/Password")
            time.sleep(2)
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logout Successful')
        time.sleep(2)
        return render(request, 'home.html')
