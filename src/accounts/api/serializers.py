from rest_framework import serializers 
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings
from django.db.models import Q

import datetime
from django.utils import timezone

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expires = api_settings.JWT_REFRESH_EXPIRATION_DELTA

User = get_user_model()

class UserPublicSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = ['id','username']


class UserRegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(style={'input_type':'password'},write_only=True)
	password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
	token = serializers.SerializerMethodField(read_only=True)
	expires = serializers.SerializerMethodField(read_only=True)
	message = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = User
		fields = [
		'username',
		'email',
		'password',
		'password2',  
		'token',
		'expires',
		'message',
		]
		extra_kwargs =  {'password':{'write_only':True}}
	
	def get_message(self,obj):
		return 'Thank you for registering. Please verify'

	def validate(self,data):
		pw = data.get('password')
		pw2 = data.pop('password2')
		if pw != pw2:
			raise serializers.ValidationError("Passwords do not match!")
		return data

	def get_token(self,obj): #requires SeralizerMethodField
		user = obj
		payload = jwt_payload_handler(user)
		context = self.context # context from the view 
		request = context.get('request') #passed request through  context from view
		print(request.META)
		token = jwt_encode_handler(payload)
		return token

	def get_expires(self,obj):
		return timezone.now() + expires - datetime.timedelta(seconds=200)

	def create(self,validated_data):
		user_obj = User.objects.create(
					username = validated_data.get('username'),
					email=validated_data.get('email'))
		user_obj.set_password(validated_data.get('password'))
		user_obj.save()
		return user_obj