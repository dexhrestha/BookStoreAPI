from django.conf.urls import url,include
from book import views

urlpatterns=[
		url(r'^$',views.BookListAPIView.as_view(),name='list'),
		url(r'^(?P<id>\d+)/',views.BookDetailAPIView.as_view(),name='detail')
		# url(r'^rest-auth/',include('rest_auth.urls')),
		# url(r'^rest-auth/registration/',include('rest_auth.registration.urls'))
]
