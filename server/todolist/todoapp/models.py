from django.db import models

# Create your models here.


class TodoItems(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    priority = models.CharField(max_length=50)
    
    
    