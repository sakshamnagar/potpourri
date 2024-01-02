from django.db import models

# Create your models here.
class Area(models.Model):
    
    Name=models.CharField(max_length=20)
    Pincode=models.DecimalField(
        default="",max_digits=6,decimal_places=0,
    )
    City_Name=models.ForeignKey("City.City",on_delete=models.CASCADE)


    def __str__(self):
        return self.Name