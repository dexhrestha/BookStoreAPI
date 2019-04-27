
import datetime
from django.utils import timezone
from django.conf import settings
from rest_framework_jwt.settings import api_settings
#set JWT_RESPONSE_PAYLOAD_HANDLER to this function 
#for custom response on jwt auth
expires = api_settings.JWT_REFRESH_EXPIRATION_DELTA

def jwt_response_payload_handler(token,user=None,request=None):
	return({
		'token':token,
		'user':user.username,
		'expires': timezone.now() + expires - datetime.timedelta(seconds=200)
	})