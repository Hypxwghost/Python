from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True) # nome da url Ex: site/blog/alguma-coisa
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
