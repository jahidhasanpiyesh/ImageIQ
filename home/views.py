from django.shortcuts import render
from .forms import ImageForm
# Create your views here.
def home(req):
    if req.method == 'POST':
        form = ImageForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            form = ImageForm()
    else:
        form = ImageForm() 
    return render(req, 'home/home.html', {'form': form}) 