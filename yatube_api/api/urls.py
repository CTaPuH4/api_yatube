from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)

v1_comment_router = DefaultRouter()
v1_comment_router.register('comments', CommentViewSet)


urlpatterns = [
    path('v1/api-token-auth/', obtain_auth_token),
    path('v1/', include(v1_router.urls)),
    path('v1/posts/<int:post_id>/', include(v1_comment_router.urls)),
]
