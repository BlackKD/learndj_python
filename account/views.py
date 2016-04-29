from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

# Create your views here.
def signin_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username,email,password)
            login(request,user)
        except IntegrityError:
            signin_error = {
                'email': email,
                'username': username,
                'password': password,
                'error_message': 'user exists'
            }
            return render(request, 'home.html', {'signin_error': signin_error})
    return redirect(request.META.get('HTTP_REFERER'))

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        login_error = {
            'username': username,
            'password': password,
            'error_message':'auth fail'
        }
        if user is None:
            return render(request,'home.html',{'login_error':login_error})
        else:
            login(request,user)
    return redirect(request.META.get('HTTP_REFERER'))

def logout_view(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))
