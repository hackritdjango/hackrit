from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class TimeStampedModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True,editable=False)
	updated_at = models.DateTimeField(auto_now=True,editable=False)


class Complaint(TimeStampedModel):	
	name = models.CharField(max_length=200)
	designation = models.CharField(max_length=200)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, related_name="posts",
		on_delete=models.CASCADE)
	office_address = models.TextField()
	Crime = models.CharField(max_length=200)
	description = models.TextField()
	proof = models.FileField(upload_to="unmask/",null=True,blank=True)
	complaint_to = models.CharField(max_length=200,editable=False,default="bivinvvpacoeg@gmail.com")
	def __str__(self):
		return self.name

class Compuser(AbstractBaseUser):
	name = models.CharField(max_length=200)
	address = models.TextField()
	identity_card_type = models.CharField(max_length=200)
	identity_card_no = models.CharField(max_length=200)