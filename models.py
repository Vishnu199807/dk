from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)