from django.db import models

# Create your models here.
class Designer(models.Model):
	Category = models.CharField(max_length = 30)
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	email = models.EmailField()
	Mobile_number = models.CharField(max_length = 13)
	Profile_pic = models.ImageField(upload_to="DesignerProfilePic")
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.first_name





class DesignerBill(models.Model):
	product_name = models.ManyToManyField("Product.Product", blank=True)
	username = models.CharField(max_length=150)
	user_phone = models.CharField(max_length=150)
	user_address = models.TextField()
	Payment_status = models.BooleanField(default=False)
	Payment_total = models.CharField(max_length=15)
