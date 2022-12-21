from django.urls import include, path

from api.views import PostViewSet, GroupViewSet, CommentViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments'
                )


app_name = 'api'

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
