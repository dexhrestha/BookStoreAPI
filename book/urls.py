from django.conf.urls import url,include
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from book import views
from users import views as UsersView
shcema_view  = get_schema_view(title='Book API')

router = DefaultRouter()
router.register(r'books',views.BookViewSet)
router.register(r'users',UsersView.UserListView)
router.register(r'reviews',views.ReviewViewSet)

urlpatterns=[
		url(r'^',include(router.urls)),
		url(r'^schema/$',shcema_view),
		url(r'^rest-auth/',include('rest_auth.urls')),
		url(r'^rest-auth/registration/',include('rest_auth.registration.urls'))
]
urlpatterns += [url(r'^api-auth/',include('rest_framework.urls')),]
