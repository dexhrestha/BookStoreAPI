from django.contrib.auth import get_user_model
from .serializers import UserDetailSerializer
from status.api.serializers import StatusInlineUserSerializer
from status.models import Status
from rest_framework import (generics,
							#pagination
							)


User = get_user_model()

class UserDetailAPIView(generics.RetrieveAPIView):
	permission_classes = []
	serializer_class = UserDetailSerializer
	queryset = User.objects.filter(is_active=True)
	lookup_field = 'username'

	def get_serializer_context(self,*args,**kwargs):
		return {'request':self.request}

class UserStatusAPIView(generics.ListAPIView):
	
	serializer_class = StatusInlineUserSerializer
	# pagination_class = pagination.PageNumberPagination
	
	def get_queryset(self,*args,**kwargs):
		username = self.kwargs.get('username',None)
		if username is None:
			return Status.objects.none()
		return Status.objects.filter(user__username=username)