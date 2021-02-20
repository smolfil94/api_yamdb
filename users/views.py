from random import choice
from string import ascii_letters

from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action, api_view, permission_classes

from .models import User
from .permissions import SiteAdminPermission
from .serializers import UserSerializers
from django.conf import settings

generator = default_token_generator


@api_view(['POST'])
@permission_classes([AllowAny])
def get_token(request):
    email = request.data.get('email')
    user = get_object_or_404(User, email=email)
    code = request.data.get('confirmation_code')
    if generator.check_token(user, code):
        refresh = RefreshToken.for_user(user)
        tokens = {'refresh': str(refresh),
                  'access': str(refresh.access_token)}
        return Response(tokens, status.HTTP_200_OK)

    return Response({"message": "неверный код подтверждения."},
                    status.HTTP_400_BAD_REQUEST)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_field = 'username'
    permission_classes=[IsAuthenticated, SiteAdminPermission]

    def perform_update(self, serializer):
        serializer.save(data=self.request.data)

    def profile(self):
        pass
