from django.db import models

# Create your models here.
class Feedback(models.Model):
    First_Name=models.CharField(max_length=20)
    Last_Name=models.CharField(max_length=20)
    Email=models.EmailField(unique=True)
    Comment=models.TextField(max_length=100)

