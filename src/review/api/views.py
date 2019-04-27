from rest_framework import generics,mixins,permissions
from django.db.models import Q

from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter,SearchFilter

from .serializers import ReviewSerializer,ReviewDetailSerializer
from review.models import Review


class ReviewListAPIView(generics.ListAPIView,mixins.CreateModelMixin):
	serializer_class = ReviewSerializer
	# permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
	# queryset = Review.objects.all()
	filter_backends = (filters.DjangoFilterBackend,SearchFilter,)
	filter_fields = ['user__username','book__title','book']

	def get_queryset(self,*args,**kwargs):
		queryset_list = Review.objects.all()
		query = self.request.GET.get('q')
		if query:
			queryset_list = queryset_list.filter(
				Q(content__icontains=query)).distinct()

		return queryset_list

	def perform_create(self,serializer):
		
		serializer.save(user=self.request.user)


	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

class ReviewDetailAPIView(generics.RetrieveAPIView,
						mixins.UpdateModelMixin,
						mixins.DestroyModelMixin):

	queryset = Review.objects.all()
	serializer_class = ReviewDetailSerializer
	lookup_field='id'

	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)
	
	def patch(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)


	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)		
