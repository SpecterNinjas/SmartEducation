from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == 'POST':
        login_username = request.POST.get('login_username')
        login_password = request.POST.get('login_password')
        user = authenticate(username=login_username, password=login_password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('main:main')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print(f"They used username: {login_username} and password: {login_password}")
            return HttpResponse("Invalid login details given")
    else:
        print("Incorrect Password GET Method")
    return render(request, 'main/index.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('main:main')

