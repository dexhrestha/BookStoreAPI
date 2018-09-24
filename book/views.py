from django_filters import rest_framework as filters
from book.models import Book,Review
from book.serializers import BookSerializer,ReviewSerializer
from rest_framework import permissions,viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.reverse import reverse
from book.permissions import IsOwnerOrReadOnly
from rest_framework.filters import OrderingFilter,SearchFilter
# class ReviewFilter(filters.FilterSet):
# 	class Meta:date
# 		model = ReviewSerializer
# 		fields=['id',]

# class BookFilter(filters.FilterSet):
# 	min_price = filters.NumberFilter(field_name='price',lookup_expr='gte')
# 	max_price = filters.NumberFilter(field_name='price',lookup_exp='lte')
# 	class Meta:
# 		model = Book
# 		fields = ['author','genre','price']

class BookViewSet(viewsets.ModelViewSet):
	#This view set automatically provides list,create,retrieve,update and destroy actions
	queryset = Book.objects.all()
	serializer_class =  BookSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	filter_backends = (filters.DjangoFilterBackend,SearchFilter)
	# filterset_class = BookFilter
	filter_fields=['author','genre','price']
	search_fields=['title',]	
	#WE can use @ action decorator if we need to create custom action

class ReviewViewSet(viewsets.ModelViewSet):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
	filter_backends = (filters.DjangoFilterBackend,OrderingFilter,SearchFilter)
	# filterset_class = ReviewFilter
	filter_fields=['book__id','writtenBy__id']
	ordering_fields=['date']
	search_fields=['book__title']
