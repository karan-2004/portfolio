from django.db import models

# Create your models here.
class certificates(models.Model):
    certificates_images = models.ImageField(upload_to='certificates')
    description = models.TextField()


    