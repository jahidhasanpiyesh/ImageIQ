from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
import re                        # ← regex সার্চের জন্য

from .forms import ImageForm
from .models import Image


# ---------------- Home: Upload + Search ----------------
def home(request):
    # ---- Upload ----
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Log in first!')
            return redirect('login')

        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.user = request.user
            img.save()
            messages.success(request, 'Image uploaded!')
            return redirect('home')
    else:
        form = ImageForm()

    # ---- Search ----
    query_raw = request.GET.get('search', '')
    query = query_raw.strip()

    if query:
        # word‑boundary regex: exact keyword match within comma‑separated list
        regex = r'\b{}\b'.format(re.escape(query))
        images = Image.objects.filter(
            Q(keywords__iregex=regex) |    # keywords ক্ষেত্র
            Q(caption__icontains=query)    # caption ক্ষেত্র
        ).order_by('-date')
    else:
        images = Image.objects.all().order_by('-date')

    context = {
        'form': form,
        'img': images,
        'search_query': query_raw,
    }
    return render(request, 'home/home.html', context)


# ---------------- Auth: Login ----------------
def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('home')
        messages.error(request, 'Invalid credentials')
        return redirect('login')
    return render(request, 'home/login.html')


# ---------------- Auth: Signup ----------------
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1    = request.POST.get('password1')
        pass2    = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request, 'Passwords do not match!')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return redirect('signup')

        User.objects.create_user(username=username, password=pass1)
        messages.success(request, 'Account created! Please log in.')
        return redirect('login')

    return render(request, 'home/signup.html')


# ---------------- Auth: Logout ----------------
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('login')
