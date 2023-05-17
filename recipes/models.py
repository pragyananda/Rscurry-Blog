from django.db import models
from datetime import datetime, date 

class recipe(models.Model):
    recipe_title=models.CharField(max_length=50)
    recipe_image=models.FileField(upload_to="recipes/",max_length=255,null=True,default=None)
    recipe_date=models.DateField(auto_now_add=False, auto_now=False, blank=True)
    recipe_des=models.TextField()
    recipe_preparetime=models.CharField(max_length=10)
    recipe_cooktime=models.CharField(max_length=10)
    recipe_servings=models.CharField(max_length=10)
    recipe_readyin=models.CharField(max_length=10)
    recipe_youtubelink=models.CharField(max_length=255)
    recipe_ingredients=models.TextField()
    recipe_rating=models.SmallIntegerField()
    recipe_comment=models.CharField(max_length=50)


# Create your models here.
