from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import SignUpForm, SignInForm, ClubCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Club
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


# Create your views here.

def user_dashboard(request):
    """Show user dashbaord."""
    data = {'user': request.user}
    return render(request, 'user_dashboard.html', data)


@login_required
def user_profile(request):
    data = {'user': request.user}
    return render(request, 'user_profile.html', data)

def home(request):
    return render(request, 'home.html')

def group(request):
    return render(request, 'group.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password_confirmation'])
            user.save()
            login(request, user)
            return redirect('user_dashboard')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            passwordEnter = form.cleaned_data.get('password')
            user = authenticate(username=username, password=passwordEnter)
            if user is not None:
                login(request, user)
                return redirect('user_dashboard')

    form = SignInForm()
    return render(request, 'sign_in.html', {'form': form})

def club_creation(request):
    """Allow user to create club."""
    if request.method == 'POST':
        form = ClubCreationForm(request.POST)
        if form.is_valid():
            # The club-creation form is valid, we save the club to the database
            form.save()
            messages.add_message(request, messages.SUCCESS, "Club created successfully.")
            return redirect('group')
        else:
            messages.add_message(request, messages.ERROR, "This club name is already taken, please choose another one.")
    else:
        form = ClubCreationForm(initial = {'owner': request.user})
    return render(request, 'new_club.html', {'form': form})
