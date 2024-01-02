from django.db import models

# Create your models here.
class City(models.Model):
   
    Name=models.CharField(max_length=20)
    State_Name=models.ForeignKey("State.State",on_delete=models.CASCADE)


    def __str__(self):
        return self.Name