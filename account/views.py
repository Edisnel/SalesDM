from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'],
                                password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                    #return render(request, 'account/login.html', {'form': form, 'autenticado': 1})
                else:
                    return HttpResponse('Disabled account')
                    #return render(request, 'account/login.html', {'form': form, 'autenticado':2})
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


def principal(request):
    return render(request, 'main/mainpage.html')

def contact(request):
    return render(request, 'main/contact.html')

def product(request):
    return render(request, 'main/product.html')

def services(request):
    return render(request, 'main/services.html')

def aboutus(request):
    return render(request, 'main/about.html')

@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})
















