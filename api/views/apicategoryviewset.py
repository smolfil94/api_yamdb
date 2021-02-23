from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from .createreadanddeleteviewset import CreateReadAndDeleteModelViewSet
from ..models import Category
from ..permissions import IsAdminOrReadOnly
from ..serializers.categoryserializer import CategorySerializer


class APICategoryViewSet(CreateReadAndDeleteModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly,]

