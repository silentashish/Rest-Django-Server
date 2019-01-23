from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from django.views.static import serve
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet


from . import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)
router.register('image',views.ImageFieldViewSet)
router.register('imagetk',views.ImageViewSet)
router.register('comment',views.CommentFieldViewSet)
router.register('token',views.TokenViewSet)
router.register('devices', FCMDeviceAuthorizedViewSet)

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls)),
    url(r'^docs/', include_docs_urls(title='Polls API')),

]
