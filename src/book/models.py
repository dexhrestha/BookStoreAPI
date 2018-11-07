from django.db import models
from datetime import datetime
from comment.models import Comment
from django.contrib.contenttypes.models import ContentType
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
	overview = models.TextField()
	
	def __str__(self):
		return str(self.author+' - '+self.title)

	@property
	def comments(self):
		instance = self
		qs=Comment.objects.filter_by_instance(instance)
		return qs

	@property
	def get_content_type(self):
		instance = self
		content_type=ContentType.objects.get_for_model(instance)
		return content_type