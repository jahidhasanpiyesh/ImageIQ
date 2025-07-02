from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model  = Image
        fields = ['photo', 'caption', 'keywords']
        widgets = {
            'photo':    forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'caption':  forms.TextInput(attrs={'class': 'form-control'}),
            'keywords': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'e.g. computer,laptop'}),
        }
