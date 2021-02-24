from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from ..models import Genre
from ..permissions import IsAdminOrReadOnly
from ..serializers.genreserializer import GenreSerializer
from .createreadanddeleteviewset import CreateReadAndDeleteModelViewSet


class APIGenreViewSet(CreateReadAndDeleteModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]
