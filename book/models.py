from django.db import models
from datetime import datetime
from users import models as userModel
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
		return str(self.author)


class Review(models.Model):
	#total dependency if Book is deleted review is deleted
	book = models.ForeignKey(Book,on_delete=models.CASCADE)
	review = models.TextField()
	date = models.DateTimeField(auto_now=True)
	writtenBy = models.ForeignKey(userModel.CustomUser,default=1,on_delete=models.CASCADE)

	def __str__(self):
		return self.writtenBy