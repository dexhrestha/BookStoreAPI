from rest_framework import serializers
from book.models import Book
from book.models import GENRE_CHOICES
from comment.api.serializers import CommentSerializer
from comment.models import Comment


class BookDetailSerializer(serializers.ModelSerializer):
	comments = serializers.SerializerMethodField()
	class Meta:
		model = Book
		fields = ('id',
			'title',
			'author',
			'overview',
			'publication',
			'quantity',
			'price',
			'genre',
			'comments')

	def get_comments(self,obj):
		comments_qs = Comment.objects.filter_by_instance(obj)
		comments = CommentSerializer(comments_qs,many=True).data
		return comments

class BookListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ('id',
			'title',
			'author',
			'publication',
			'quantity',
			'price',
			'genre',)
