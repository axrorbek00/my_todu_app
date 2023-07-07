from django.shortcuts import render, redirect
from .forms import RegistrationModelForm, LoginForms
from .models import UsersModel
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib import messages


def profile_view(request):
    return render(request, 'main/profile.html')


def Logout_View(request):
    logout(request)
    return redirect('home')


def LoginForms_Views(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.info(request, f'{user.username} Xush kelibsiz')
                return redirect('todu_list')
        raise ValidationError('Parol yoki Username xato', 'password')
    return render(request, 'main/login.html', context={
        'login_form': form
    })


def Registration_view(request):
    form = RegistrationModelForm()
    if request.method == 'POST':
        form = RegistrationModelForm(data=request.POST)
        if form.is_valid():
            user = UsersModel(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                last_name=form.cleaned_data['last_name'],
                first_name=form.cleaned_data['first_name'],
                password=make_password(form.cleaned_data['password'])

            )
            user.save()
            messages.success(request, "Ro'yxatdan muffaqyatli o'tdingiz")
            return redirect('login')
    return render(request, 'main/registration.html', context={
        'registration_form': form
    })
