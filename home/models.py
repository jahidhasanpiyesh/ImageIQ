from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Image(models.Model):
    photo = models.ImageField(upload_to='myimages') # Field to store the image file, uploaded to 'myimages' directory.
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.category.name} - {self.photo.name}"
    
    