from django.shortcuts import render, HttpResponse, redirect
from .forms import userform, registerform
from .models import UserCust
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'game/home.html')

#def login(request):
#    username = request.POST['username']
#    password = request.POST['password']
#    user = authenticate(request, username=username, password=password)
#    if user is not None:
#        login(request, user)
#    else:

def register(request):
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            custuser = UserCust.objects.create(username=username, email=email, password=password, current_location_id=1)
            return redirect('index')

    else:
        form = registerform()
    
    return render(request, 'game/register.html', {'form':form})