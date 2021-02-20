from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router_v1 = DefaultRouter()

urlpatterns = [
   # path('v1/auth/email/', views.email_confirmation),
    path('v1/auth/token/', views.get_token),
    ]