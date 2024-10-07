from rest_framework import viewsets, permissions, generics, status
from .serializers import *
from .models import *
from .filters import MovieFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import CheckOwner


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers


class UserProfileSimpleViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSimpleSerializers


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers


class DirectorListViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorListSerializers


class DirectorDetailViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorDetailSerializers


class ActorListViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializers


class ActorDetailViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializers


class JanreViewSet(viewsets.ModelViewSet):
    queryset = Janre.objects.all()
    serializer_class = JanreSerializers


class MovieListViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilter
    search_fields = ['movie_name']
    ordering_fields = ['year']
    permission_classes = [permissions.IsAuthenticated, CheckOwner]


class MovieDetailViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MoviePhotos(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MoviePhotosSerializers


class MovieLanguagesViewSet(viewsets.ModelViewSet):
    queryset = MovieLanguages.objects.all()
    serializer_class = MovieLanguagesSerializers


class MomentsViewSet(viewsets.ModelViewSet):
    queryset = Moments.objects.all()
    serializer_class = MomentsSerializers


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializers


class FavoriteMovieViewSet(viewsets.ModelViewSet):
    queryset = FavoriteMovie.objects.all()
    serializer_class = FavoriteMovieSerializers


class HistoryListViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistoryDetailSerializers


class HistoryDetailViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistoryListSerializers