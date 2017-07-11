from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from . models import *
from django.db.models import Count
import re
EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    print("*"*50)
    return render(request, 'exchange_platform/index.html')

<<<<<<< HEAD
def baseball(request):
    return render(request, 'exchange_platform/baseball.html')
=======
def login_page(request):
    context = {}
    if 'invalid_login' in request.session:
        request.session.pop('invalid_login')
        context['login_messages'] = True
    elif 'invalid_registration' in request.session:
        request.session.pop('invalid_registration')
        context['registration_messages'] = True

    return render(request, 'exchange_platform/login_page.html', context)

def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            request.session['email'] = request.POST['email']

            if user.password==request.POST['password']:
                request.session['first_name'] = user.first_name
                return redirect ('exchange_platform:index')
            else:
                request.session['invalid_login'] = True
                messages.add_message(request, messages.ERROR,"Password is invalid.")
                return redirect('exchange_platform:login_page')
        except:
            request.session['invalid_login'] = True
            messages.add_message(request, messages.ERROR,"That email is not registered!")
            return redirect('exchange_platform:login_page')

def register(request):
    if request.method == 'POST':
        isValid=True
        if len(request.POST['first_name']) < 1:
            messages.add_message(request, messages.ERROR, "Please enter your first name.")
            isValid = False
        elif not request.POST['first_name'].isalpha():
            messages.add_message(request, messages.ERROR,"Please enter a valid first name.")
            isValid = False

        if len(request.POST['last_name']) < 1:
            messages.add_message(request, messages.ERROR, "Please enter your last name.")
            isValid = False
        elif not request.POST['last_name'].isalpha():
            messages.add_message(request, messages.ERROR,"Please enter a valid last name.")
            isValid = False

        if len(request.POST['email']) < 1:
            messages.add_message(request, messages.ERROR, "Please enter a valid email.")
            isValid = False
        elif not EMAIL_REGEX.match(request.POST['email']):
            messages.add_message(request, messages.ERROR, "Invalid Email. Please Re-Enter! ")
            isValid = False

        if len(request.POST['password']) < 9:
            messages.add_message(request, messages.ERROR, "Password must be longer than 8 characters.")
            isValid = False
        elif request.POST['password'] != request.POST['confirm_password']:
            messages.add_message(request, messages.ERROR, "Password and Confirm do not match!")
            isValid = False

        if not isValid:
            request.session['invalid_registration'] = True
            return redirect('/')
        else:
            new_user = User.objects.create(first_name=request.POST['first_name'],aka=request.POST['aka'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
            request.session['first_name']=new_user.first_name
            request.session['email']=new_user.email
            return redirect('exchange_platform:index')

def logout(request):
    request.session.clear()
    return redirect('/')
>>>>>>> 63a8fe92f81eb590b80f6f35c1265fcbf6769994
