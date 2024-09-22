from django.urls import include, path
from rest_framework_nested import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

comment_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
comment_router.register('comments', CommentViewSet)


urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),
    path('', include(comment_router.urls)),
]
