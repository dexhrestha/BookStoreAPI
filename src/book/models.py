from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
GENRE_CHOICES = [('Sci-Fi','Sci-Fi'),('Comedy','Comedy')]
# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=256)
	author = models.CharField(max_length=100)
	publication = models.CharField(max_length=100)
	quantity = models.IntegerField()
	price = models.FloatField()
	genre = models.CharField(choices=GENRE_CHOICES,max_length=100,default='Sci-Fi')
	
	def __str__(self):
		return str(self.author+' - '+self.title)

