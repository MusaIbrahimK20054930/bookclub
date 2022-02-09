from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm
from .forms import SignInForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def sign_up(request):
    form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def sign_in(request):
    form = SignInForm()
    return render(request, 'sign_in.html', {'form': form})
