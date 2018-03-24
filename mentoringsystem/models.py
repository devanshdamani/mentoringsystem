from django.db import models
from django.utils import timezone

class Student(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	sid = models.DecimalField
	fname = models.CharField(max_length=30)
	mname = models.CharField(max_length=30)
	lname = models.CharField(max_length=30)
	phonenumber = models.DecimalField
	address = models.TextField()
	published_date = models.DateTimeField(blank=True, null=True)

def publish(self):
	self.published_date = timezone.now()
	self.save()

def __str__(self):
	return self.sid