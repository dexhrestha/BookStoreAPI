from rest_framework import serializers
from book.models import Book
from book.models import GENRE_CHOICES



class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ('id','title','author','publication','quantity','price','genre')
