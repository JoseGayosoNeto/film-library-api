from django.db.models import Avg
from rest_framework import serializers
from actors.models import NATIONALITY_CHOICES
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1888:
            raise serializers.ValidationError('Release date cannot be less than 1888.')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Resume must not be longer than 200 characters.')
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):

        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return f'{rate:.1f}/5.0'

        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        actors_data = data.get('actors', [])
        for actor in actors_data:
            nationality_abbr = actor.get('nationality', '')
            nationality_fullname = dict(NATIONALITY_CHOICES).get(nationality_abbr, '')
            actor['nationality'] = nationality_fullname

        data['actors'] = actors_data

        return data


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
