from rest_framework.viewsets import ModelViewSet

from ..models import Title
from ..serializers.titleserializer import TitleSerializer


class APITitleViewSet(ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
