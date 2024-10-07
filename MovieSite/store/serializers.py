from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age',
                   'phone_number', 'status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name, last_name']


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name', 'last_name', 'first_name']


class DirectorDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = [' director_name', 'bio', 'age', 'director_image']


class ActorListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name', 'first_name']


class ActorDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name', 'bio', 'age', 'actor_image']


class JanreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Janre
        fields = ['janre_name']


class MoviePhotosSerializers(serializers.ModelSerializer):
    class Meta:
        model = MoviePhotos
        fields = ['movie', 'image']


class MovieLanguagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video', 'movie']

    def get_average_rating(self, obj):
        return obj.get_average_rating()

class MomentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie', 'movie_moments']


class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['user', 'movie', 'stars', 'parent_review', 'text', 'created_date']


class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteMovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'


class HistoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['viewed_at']


class HistoryDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['user', 'movie', 'viewed_at']


class MovieListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'movie_name',]

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class MovieDetailSerializers(serializers.ModelSerializer):
    country = CountrySerializers()
    ratings = RatingSerializers(many=True, read_only=True)
    movie = MoviePhotosSerializers(many=True, read_only=True)


    class Meta:
        model = Movie
        fields = ['movie_name', 'movie', 'country', 'description', 'year', 'average_rating', 'ratings']

    def get_average_rating(self, obj):
        return obj.get_average_rating()
