from django.db import models

# Create your models here.

class ImagesModel(models.Model):
    images = models.ImageField(upload_to='')