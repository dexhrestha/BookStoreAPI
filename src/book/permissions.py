from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
	#Custom permission to only allow owners of an object 

	def has_permission(self,request,view):
		if request.method in permissions.SAFE_METHODS:
			return True
		else:
			return request.user.is_staff == True
