from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from .models import logger, article
from django.contrib.auth.models import User
def index(request):
    
    return render(request, 'index.html')


def logins(request):
    
    return render(request, 'login.html')


@login_required(login_url="/login/")
def log(request):

    logss = logger.objects.all()
    firstname = logss[0].first_name
    lastname = logss[0].last_name
    phone = logss[0].phone_number
    occupation = logss[0].occupation
    email = logss[0].email
    username = logss[0].username
   
    return render(request, 'profile.html', {"logss": logss, "firstname": firstname,": lastname": lastname,
    "occupation": occupation,
    "email": email,
    "username": username,
    "phone": phone })



@login_required(login_url="/login/")
def home(request):
    
    a_list = article.objects.all()
    t = a_list[1]
        
   

    return render(request, 'home.html', {"a_list": a_list, "t": t})

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm

# Create your views here
class UserRegisterView(generic.CreateView):
    
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    

