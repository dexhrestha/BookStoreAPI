from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from . import models
from . import serializers

class UserListView(viewsets.ReadOnlyModelViewSet):
	queryset = models.CustomUser.objects.all()
	serializer_class = serializers.UserSerializer
	