from django_filters import rest_framework as filters
from book.models import Book
from book.serializers import BookSerializer	
from rest_framework import permissions,authentication,generics,mixins
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.reverse import reverse
from book.permissions import IsAdminUserOrReadOnly
from rest_framework.filters import OrderingFilter,SearchFilter

class BookListAPIView(generics.ListAPIView,mixins.CreateModelMixin):
	#This view set automatically provides list,create,retrieve,update and destroy actions
	queryset = Book.objects.all()
	serializer_class =  BookSerializer
	permission_classes = (IsAdminUserOrReadOnly,)
	filter_backends = (filters.DjangoFilterBackend,SearchFilter)
	# filterset_class = BookFilter
	filter_fields=['author','genre','price']
	search_fields=['title',]	

	def post(self,request,*args,**kwargs):
		print(request.user.is_staff)
		return self.create(request,*args,**kwargs)


class BookDetailAPIView(mixins.UpdateModelMixin,
						mixins.DestroyModelMixin,
						generics.RetrieveAPIView):

	permission_classes = (IsAdminUserOrReadOnly,)
	queryset = Book.objects.all()
	lookup_field = 'id'
	serializer_class = BookSerializer

	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def patch(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)