from django.conf.urls import url,include
from .views import UserDetailAPIView,UserStatusAPIView

urlpatterns = [
	url(r'^(?P<username>\w+)/$',UserDetailAPIView.as_view(),name='user-detail'),
	url(r'^(?P<username>\w+)/status',UserStatusAPIView.as_view(),name='user-status-list'),
]