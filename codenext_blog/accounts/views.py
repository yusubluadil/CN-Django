from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Profile
from .forms import ProfileForm


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, f'Xoş gəldin, {user.username}')
            return redirect('all_blogs')
        else:
            messages.info(request, 'Daxil etdiyiniz məlumatlara uyğun istifadəçi tapılmadı')

    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('all_blogs')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            # Bu cür yanaşma tam da doğru sayılmaz! 
            # Signals ilə yazın
            # user = User.objects.get(username=form.cleaned_data.get('username'))
            # Profile.objects.create(user=user)

            return redirect('all_blogs')
        messages.error(request, form.errors)
        return redirect('register')
    else:
        form = UserCreationForm()
        return render(request, 'accounts/register.html', {'creation_form': form})


def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        ...
    else:
        form = ProfileForm(instance=profile)
        return render(request, 'accounts/profile.html', {'profile_form': form})
