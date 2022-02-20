from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import SignUpForm
from .forms import SignInForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, 'home.html')

def info(request):
    return render(request, 'info.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password_confirmation'])
            user.save()
            login(request, user)
            return redirect('info')
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
                return redirect('info')

    form = SignInForm()
    return render(request, 'sign_in.html', {'form': form})
