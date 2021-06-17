from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	owner = models.OneToOneField(User,related_name='owner', on_delete=models.CASCADE, primary_key=True)
	members = models.ManyToManyField(User,db_column="user", related_name='members')

	


class File(models.Model):
	name = models.CharField(max_length=30)
	file = models.FileField()
	
	def __str__(self):
		return self.name