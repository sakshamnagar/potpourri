from django.db import models

# Create your models here.
class Contact(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField(unique=True)
    Subject=models.CharField(max_length=30)
    Message=models.TextField(max_length=150)

    
