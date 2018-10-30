from rest_framework import serializers 
from django.contrib.auth import get_user_model
from status.api.serializers import StatusInlineUserSerializer
from rest_framework.reverse import reverse as api_reverse
User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
	# recent_status = serializers.SerializerMethodField(read_only=True)
	# status_uri = serializers.SerializerMethodField(read_only=True)
	status = serializers.SerializerMethodField(read_only=True)
	uri = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = User
		fields = ['id','username','status','uri']

	# def get_recent_status(self,obj):
	# 	print(obj.is_authenticated())
	# 	qs = obj.status_set.all().order_by('-timestamp')[:2] #Status.objects.filter(username=obj)
	# 	return StatusInlineUserSerializer(qs,many=True).data

	# def get_status_uri(self,obj):
	# 	return self.get_uri(obj) + '/status'

	def get_uri(self,obj):
		request = self.context.get('request')
		return api_reverse("api-user:user-detail",kwargs={"username":obj.username},request=request)
	def get_status(self,obj):
		qs = obj.status_set.all().order_by('-timestamp')
		request = self.context.get('request')
		limit = 10
		# print(request.GET.get('limit'))
		if request.GET.get('limit'):
			limit = int(request.GET.get('limit'))
		data = {
			'uri':self.get_uri(obj)+"status/",
			'last':StatusInlineUserSerializer(qs.first(),context={'request':request}).data,
			'recent':StatusInlineUserSerializer(qs[:limit],context={'request':request},many=True).data,
					}
		return data