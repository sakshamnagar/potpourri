from django.db import models

# Create your models here.
class State(models.Model):
    
    Name=models.CharField(max_length=20)
    Status=models.CharField(
        max_length=1,
        choices=(
            ('0','Inactive'),
            ('1','Active'),
        ),default="1"
    )


    def __str__(self):
        return self.Name