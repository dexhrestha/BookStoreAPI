from django.db import models
from django.contrib.auth import get_user_model
from book.models import Book
User = get_user_model()
# Create your models here.
class ReviewQuerySet(models.QuerySet):
	pass

class ReviewManager(models.Manager):
	pass

class Review(models.Model):
	user =  models.ForeignKey(User,on_delete=models.CASCADE)
	book = models.ForeignKey(Book,on_delete=models.CASCADE)
	title = models.CharField(max_length=128)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add = True)
	
	objects = ReviewManager()
	
	def __str__(self):
		return self.user.username+' '+self.content[:5]

	class Meta:
		ordering = ['-timestamp']
