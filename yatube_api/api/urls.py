from django.urls import include, path

from api.views import PostViewSet, GroupViewSet, CommentViewSet

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments'
                )


app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
