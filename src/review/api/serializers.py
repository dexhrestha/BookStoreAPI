from rest_framework import serializers
from review.models import Review
from book.serializers import BookListSerializer
from book.models import Book
from accounts.api.serializers import UserPublicSerializer
class ReviewSerializer(serializers.ModelSerializer):
	user = UserPublicSerializer(read_only=True)
	class Meta:
		model = Review
		fields = ['id',
				'user',
				'title',
				'book',
				'content',
				'timestamp']
		# fields = '__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):
	user = UserPublicSerializer(read_only=True)
	book = BookListSerializer(read_only=True)
	
	class Meta:
		model = Review
		fields = ['id',
				'user',
				'title',
				'book',
				'content',
				'timestamp']