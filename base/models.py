""" Basic models, such as user profile """
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):
    age = models.CharField(max_length=155,null=True,blank=True)

class SiteInfo(models.Model):
	site_name = models.CharField(max_length=155,null=False,verbose_name="Name of the web site")
	#logo = models.ImageField(upload_to = 'images/')
	description = models.TextField(max_length=10000,null=True,blank=True)
	email = models.CharField(max_length=155,null=True,blank=True)
	telephone = models.CharField(max_length=155,null=True, blank=True)
	#meta_keywords = models.TextField(max_length=155,null=True,blank=True)
	#meta_description = models.TextField(max_length=155,null=True,blank=True)
	#meta_author = models.CharField(max_length=155,null=True,blank=True)
	
	# twitter_url = models.CharField(max_length=155,null=True, blank=True)
	# fb_url = models.CharField(max_length=155,null=True, blank=True)
	# gplus_url = models.CharField(max_length=155,null=True, blank=True)
	# linkedin_url = models.CharField(max_length=155,null=True, blank=True)
	# instagram_url = models.CharField(max_length=155,null=True, blank=True)
	# tumblr_url = models.CharField(max_length=155,null=True, blank=True)
	
	def __unicode__(self):
		return self.site_name
	class Meta:
		verbose_name="Site Information"
		verbose_name_plural="Site Information"

class Projects(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    is_apprival = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name

