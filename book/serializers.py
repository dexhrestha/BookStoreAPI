from users import models
from rest_framework import serializers
from book.models import Book,Review
from book.models import GENRE_CHOICES



class BookSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Book
		fields = ('id','title','author','publication','quantity','price','genre')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	review = serializers.PrimaryKeyRelatedField(many=True,queryset=Review.objects.all())
	
	class Meta:
		model = models.CustomUser
		fields = ('id','username','email')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Review
		fields = ('id','book','review','date','writtenBy')