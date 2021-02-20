from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from .createreadanddeleteviewset import CreateReadAndDeleteModelViewSet
from ..models import Genre
from ..serializers.genreserializer import GenreSerializer


class APIGenreViewSet(CreateReadAndDeleteModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
