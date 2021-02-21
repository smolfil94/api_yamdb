from rest_framework import serializers

from .categoryserializer import CategorySerializer
from .genreserializer import GenreSerializer
from ..models import Title, Category, Genre


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)
    genre = GenreSerializer(many=True)

    class Meta:
        fields = '__all__'
        model = Title


class GetTitleSerializer(TitleSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()


class PostTitleSerializer(TitleSerializer):
    pass
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all(),
        required=False
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True
    )
    year = serializers.IntegerField(
        required=False,
    )
