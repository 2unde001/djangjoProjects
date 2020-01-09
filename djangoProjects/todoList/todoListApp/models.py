from django.db import models


# Create your models here.
"""
Create a model for our application
"""
class TodoItems(models.Model):
    content = models.TextField()
