from rest_framework import serializers
from ..models.genre import Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Genre
