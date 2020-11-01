from django.db import models
from users.models import CustomUser

class events (models.Model):
	date = models.DateField(auto_now_add = False)
	time = models.TimeField(auto_now=False, auto_now_add=False)
	duration = models.DurationField(null = True,blank = True)
	country = models.CharField(max_length = 255,null=False)
	topic = models.CharField(max_length = 255,null=False,unique = True)
	client = models.CharField(max_length = 255,null=False)
	website = models.URLField(max_length=255)
	emails = models.TextField()
	embeded = models.TextField()
	complete = models.BooleanField(default= False)
	status = models.BooleanField(default= False)
	notification = models.BooleanField(default= False)
	video = models.URLField(null= True)
	auto_test_creation = models.BooleanField(default = False)
	user = models.ForeignKey(CustomUser,on_delete = models.DO_NOTHING)

	class Meta:
		verbose_name_plural = 'events'

	def __str__(self):
	    return self.topic

class tests (models.Model):
	date = models.DateField(auto_now_add = False)
	time = models.TimeField(auto_now=False, auto_now_add=False)
	# duration = models.DurationField(null = True,blank = True)
	country = models.CharField(max_length = 255,null=False)
	topic = models.CharField(max_length = 255,null=False)
	client = models.CharField(max_length = 255,null=False)
	emails = models.TextField()
	complete = models.BooleanField(default= False)
	status = models.BooleanField(default= False)
	notification = models.BooleanField(default= False)
	event = models.ForeignKey(events, on_delete=models.CASCADE)
	user = models.ForeignKey(CustomUser,on_delete = models.DO_NOTHING)
	class Meta:
		verbose_name_plural = 'tests'

	def __str__(self):
	    return self.topic