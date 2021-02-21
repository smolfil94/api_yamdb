from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CodeConfirmView, EmailSignUpView, UserViewSet

router_v1 = DefaultRouter()

router_v1.register(r'users', UserViewSet, basename='users')

router_v1.register(r'users', UserViewSet)

auth_patterns = [
    path(
        'email/',
        EmailSignUpView.as_view()
    ),
    path(
        'token/',
        CodeConfirmView.as_view(),
        name='token_obtain_pair',
    ),
]

urlpatterns = [
    path('', include(router_v1.urls)),
    path(
        'v1/auth/',
        include(auth_patterns),
    ),
    path(
        'v1/',
        include(router_v1.urls),
    ),
]
