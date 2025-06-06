from django import forms
from .models import Image

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = '__all__'
#         labels = {"photo":""}


# gallery/forms.py

from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__' # Include all fields from the image model.
        labels = {"photo": ""} # Custom Lable for the photo field.
        
        # Customizing the widgets for better UI.
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}), 
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
