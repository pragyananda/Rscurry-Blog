from django.db import models

# Create your models here.
class contactform(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=60)
    subject=models.CharField(max_length=80)
    message=models.TextField()