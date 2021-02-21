from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import SAFE_METHODS
from rest_framework.viewsets import ModelViewSet

from ..filter import TitleFilter
from ..models import Title
from ..serializers.titleserializer import (TitleSerializer, GetTitleSerializer,
                                           PostTitleSerializer)


class APITitleViewSet(ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return GetTitleSerializer
        return PostTitleSerializer
