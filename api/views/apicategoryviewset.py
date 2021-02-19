from .createreadanddeleteviewset import CreateReadAndDeleteModelViewSet
from ..models import Category
from ..serializers.categoryserializer import CategorySerializer


class APICategoryViewSet(CreateReadAndDeleteModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
