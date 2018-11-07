
from django.conf.urls import url,include
from comment.api.views import CommentListAPIView,CommentDetailAPIView,CommentCreateAPIView,CommentEditAPIView
urlpatterns = [
	url(r'^$',CommentListAPIView.as_view()),
	url(r'^create/$',CommentCreateAPIView.as_view()),
	url(r'^(?P<id>\d+)/$',CommentDetailAPIView.as_view()),
	url(r'^(?P<id>\d+)/edit/$',CommentEditAPIView.as_view()),
]
