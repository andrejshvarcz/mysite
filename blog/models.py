from django.db import models
from django.utils import timezone
# Create your models here.


class GuestData(models.Model):
	ip = models.CharField(max_length=100)
	last_seen = models.DateTimeField(blank=True)
	log_attemps = models.IntegerField(default=0)

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now())
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


class UserData(models.Model):
	login = models.CharField(max_length=200, null=True)
	password = models.CharField(max_length=200, null=True)
	ip = models.CharField(max_length=200, null=True)

	def __str__(self):
		return '{}@{}'.format(self.login, self.password)
