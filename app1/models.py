from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    photo     = models.ImageField(upload_to='myimages/')
    caption   = models.CharField(max_length=255, blank=True)
    keywords  = models.CharField(max_length=255, help_text="Comma‑separated keywords (e.g. computer,laptop)")
    date      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} – {self.photo.name}"
