from django.db import models
from corruption import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.


class TimeStampedModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True,editable=False)
	updated_at = models.DateTimeField(auto_now=True,editable=False)


class Complaint(TimeStampedModel):	
	name = models.CharField(max_length=200)
	designation = models.CharField(max_length=200)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, related_name="unmask",
		on_delete=models.CASCADE)
	office_address = models.TextField()
	Crime = models.CharField(max_length=200)
	description = models.TextField()
	proof = models.FileField(upload_to="unmask/",null=True,blank=True)
	complaint_to = models.CharField(max_length=200,editable=False,default="ismailshibiliya@gmail.com")
	def __str__(self):
		return self.name

class Compuser(AbstractUser):
	first_name = models.CharField(null=False,blank=False,max_length=200,default="hai")
	last_name = models.CharField(null=False,blank=False,max_length=200,default="hai")
	address = models.TextField(null=False,blank=False,default="hai")
	identity_card_type = models.CharField(null=False,blank=False,max_length=200,default="hai")
	identity_card_no = models.CharField(null=False,blank=False,max_length=200,default="hai")
	username = models.CharField(max_length=200,default="hai",unique=True)
	email = models.CharField(max_length=200,null=False,blank=False,default="ismailshibiliya@gmail.com")