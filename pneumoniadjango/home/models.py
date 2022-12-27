from django.db import models
# models.py
class Image(models.Model):
    xray_image = models.ImageField(upload_to='') 