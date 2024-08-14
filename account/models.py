from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class User(AbstractUser):
	profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
	address_line1 = models.CharField(max_length=255)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	pincode = models.CharField(max_length=10)
	STATUS = [('Doctor','Doctor'),('Patient','Patient')]
	status = models.CharField(max_length=7,choices=STATUS)
	created = models.DateTimeField(auto_now_add=True, auto_created=True)
	updated = models.DateTimeField(auto_now=True, auto_created=True)
	def __str__(self):
	    return self.username
 

class Blog(models.Model):
	CATEGORY_CHOICES = [('Mental_Health','Mental Health'),('Heart_Disease','Heart Disease'),('Covid19','Covid19'),('Immunization','Immunization')]
	STATUS = [('Draft','Draft'),('Published','Published'),('Archived','Archived')]
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=200,null=False,blank=False)
	profile_picture = models.ImageField(upload_to='blog_images/', null=False, blank=False, default='avatar.png')
	category = models.CharField(max_length=25,choices=CATEGORY_CHOICES)
	summary = models.TextField()
	content = models.TextField(blank=False)
	status = models.CharField(max_length=15,choices=STATUS,default='Draft') 
	url= models.SlugField(max_length=500, editable=False)
	created = models.DateTimeField(auto_now_add=True, auto_created=True)
	updated = models.DateTimeField(auto_now=True, auto_created=True)

	def save(self, *args, **kwargs):
		self.url = self.title
		self.url= slugify(self.url)
		super(Blog, self).save(*args, **kwargs)
  

	def __str__(self):
	    return self.title
    