from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    #check to see if logging in

    if request.method == 'POST':
        username = request.POST['username'] #field name from a form
        password = request.POST['password'] #we assign whatever the user typed in to these variables
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('home')
        else:
            messages.success(request, 'Error logging in')
            return redirect('home')
    else:
        return render(request, 'home.html', {})



def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')