from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
	createdDateTime = models.DateTimeField(auto_now_add=True, auto_now=False)
	startDateTime = models.DateTimeField()
	endDateTime = models.DateTimeField()
	locationAddress = models.CharField(max_length=200)
	locationLattitude = models.FloatField(null=True)
	locationLongitude = models.FloatField(null=True)
	userPosted = models.ForeignKey(User, related_name='userPosted')
	userGoing = models.ForeignKey(User, related_name='userGoing')

	def __str__(self):
		return self.locationAddress