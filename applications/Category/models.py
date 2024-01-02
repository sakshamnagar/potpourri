from django.db import models

# Create your models here.
class Category(models.Model):
    
    Cat_Name=models.CharField(max_length=35)
    Cat_Image = models.ImageField(upload_to="Catimages/")
    Cat_Description = models.TextField()
    Cat_status=models.CharField(
        max_length=1,
        choices=(
            ('0','Inactive'),
            ('1','Active'),
        ),default="1"
    )

    def __str__(self):
        return self.Cat_Name
    