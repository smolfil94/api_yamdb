from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.apicategoryviewset import APICategoryViewSet
from api.views.apicommentviewset import APICommentViewSet
from api.views.apigenreviewset import APIGenreViewSet
from api.views.apireviewviewset import APIReviewViewSet
from api.views.apititleviewset import APITitleViewSet

router_v1 = DefaultRouter()

router_v1.register('titles', APITitleViewSet)
router_v1.register('genres', APIGenreViewSet)
router_v1.register('categories', APICategoryViewSet)
router_v1.register(r'titles/(?P<title_id>\d+)/reviews', APIReviewViewSet,
                   basename='Review')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    APICommentViewSet
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
