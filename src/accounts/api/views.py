from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate,get_user_model
from rest_framework_jwt.settings import api_settings
from django.db.models import Q
from rest_framework import generics
from .serializers import UserRegisterSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()
#We can authenticate user with either username or email byusing
#this custom auth apiview
class AuthView(APIView):
	permission_classes = []

	def post(self,request,*args,**kwargs):
		if request.user.is_authenticated:
			return Response({'data':'You are already authenticated'})
		data = request.data
		username = data.get('username') #username or email
		password = data.get('password')
		qs = User.objects.filter(Q(username__iexact=username)|Q(email__iexact=username)).distinct()
		if qs.count()==1: #if user exists
			user_obj = qs.first()
			if user_obj.check_password(password):
				user =user_obj
				user = authenticate(username=username,password=password)
				payload = jwt_payload_handler(user)
				token = jwt_encode_handler(payload)
				response = jwt_response_payload_handler(token,user,request=request)
				authenticate(username=username,password=password)
				print(request.user.is_authenticated)
				return Response(response,status=200)

		return Response({'detail':'Invalid Credentials'},status=401)


class RegisterAPIView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserRegisterSerializer
	permission_classes = []

	def get_serializer_context(self,*args,**kwargs): #pass request to serializer
		return {'request':self.request}

class RegisterView(APIView):
	permission_classes = []

	def post(self,request,*args,**kwargs):
		print(request.user)
		if request.user.is_authenticated:
			return Response({'data':'You are already registered and authenticated'})
		data = request.data
		username = data.get('username')
		email = data.get('email')
		password = data.get('password')
		password2 = data.get('password2')

		qs = User.objects.filter(Q(username__iexact=username)|Q(email__iexact=email))
		if password!=password2:
			return Response({'detail':'Passwords donot match'},status=401)
		if qs.exists():
			return Response({'detail':'User already exists'},status=401)
		else:
			user = User.objects.create_user(username=username,email=username)  
			user.set_password(password)
			user.save()
			authenticate(username=username,password=password)
			payload = jwt_payload_handler(user)
			token = jwt_encode_handler(payload)
			response = jwt_response_payload_handler(token,user,request=request)
			return Response(response,status=201)
		return Response({'detail':'Invalid Request'},status=400)