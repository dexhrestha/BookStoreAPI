from django.conf.urls import url,include
from .views import (
	ReviewListAPIView,
	ReviewDetailAPIView)

urlpatterns=[
		url(r'^$',ReviewListAPIView.as_view(),name='list'),
		url(r'^(?P<id>\d+)/',ReviewDetailAPIView.as_view(),name='thread'),
		]