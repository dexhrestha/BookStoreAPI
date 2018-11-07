from comment.models import Comment
from comment.api.serializers import CommentSerializer,CommentDetailSerializer,createCommentSerializer
from rest_framework import generics,mixins,permissions
from comment.api.permissions import IsOwnerOrReadOnly
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter,SearchFilter

class CommentListAPIView(generics.ListAPIView):
	# queryset = Comment.objects.parent()
	serializer_class = CommentSerializer
	filter_backends = (filters.DjangoFilterBackend,SearchFilter)
	filter_fields=['object_id','user']

	def get_queryset(self):
		qs= Comment.objects.parent()
		content_type = self.request.GET.get('type')
		if(content_type):
			qs = Comment.objects.get_by_content_type(content_type)
		return qs
	
		
class CommentDetailAPIView(generics.RetrieveAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentDetailSerializer
	lookup_field = 'id'

class CommentCreateAPIView(generics.CreateAPIView):
	queryset= Comment.objects.all()
	permission_classes = [permissions.IsAuthenticated]

	def get_serializer_class(self):
		model_type = self.request.GET.get('type')
		object_id = self.request.GET.get('id')
		# parent_id = self.request.GET.get('parent_id',None)
		return createCommentSerializer(
			model_type=model_type,
			object_id=object_id,
			# parent_id=parent_id,
			user=self.request.user)

class CommentEditAPIView(
	generics.RetrieveAPIView,
	mixins.UpdateModelMixin,
	mixins.DestroyModelMixin):
	
	queryset = Comment.objects.filter(id__gte=0)
	serializer_class = CommentDetailSerializer
	permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]
	lookup_field = 'id'

	def put(self,request,*args,**kwargs):
		return self.update(request,*args,*kwargs)

	def patch(self,request,*args,**kwargs):
		return self.update(request,*args,*kwargs)

	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,*kwargs)