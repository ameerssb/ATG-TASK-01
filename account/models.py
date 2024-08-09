from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
	address_line1 = models.CharField(max_length=255)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	pincode = models.CharField(max_length=10)

	def __str__(self):
	    return self.username