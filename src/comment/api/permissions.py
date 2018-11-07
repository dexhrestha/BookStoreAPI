from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	#Custom permission to only allow owners of an object 

	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		else:
			return request.user == obj.user
