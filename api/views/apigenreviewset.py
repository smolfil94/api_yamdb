from .createreadanddeleteviewset import CreateReadAndDeleteModelViewSet
from ..models import Genre
from ..serializers.genreserializer import GenreSerializer


class APIGenreViewSet(CreateReadAndDeleteModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
