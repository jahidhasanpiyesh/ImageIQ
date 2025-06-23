from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(req):
    if req.method == 'POST':
        form = ImageForm(req.POST, req.FILES) # Create an instance of ImageForm with POST data and files.
        # If the form is valid, save the data to the database.
        if form.is_valid():
            form.save()
    form = ImageForm() # Create a new instance of ImageForm for the empty form.
    img = Image.objects.all() # Fetch all Image objects from the database.
    return render(req, 'home/home.html', {'img':img, 'form': form}) 

def login(req):
    return render(req, 'home/login.html')

def signup(req):
    return render(req, 'home/signup.html')
    
