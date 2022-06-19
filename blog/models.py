from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    """A post in the blog"""
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now = True)
    published_date = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title
    
