from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('', MovieListViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_list'),
    path('<int:pk>/', MovieDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                  'delete': 'destroy'}), name='movie_detail'),


    path('users', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='users_list'),
    path('users/<int:pk>/', UserProfileSimpleViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                              'delete': 'destroy'}), name='users_detail'),


    path('country', CountryViewSet.as_view({'get': 'list', 'post': 'create'}), name='country_list'),
    path('country/<int:pk>/', CountryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy'}), name='country_detail'),


    path('rating', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='rating_detail'),


    path('director', DirectorListViewSet.as_view({'get': 'list', 'post': 'create'}), name='director_list'),
    path('director/<int:pk>/', DirectorDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                              'delete': 'destroy'}), name='director_detail'),


    path('actor', ActorListViewSet.as_view({'get': 'list', 'post': 'create'}), name='actor_list'),
    path('actor/<int:pk>/', ActorDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                        'delete': 'destroy'}), name='actor_detail'),


    path('janre', JanreViewSet.as_view({'get': 'list', 'post': 'create'}), name='janre_list'),
    path('janre/<int:pk>/', JanreViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                  'delete': 'destroy'}), name='janre_detail'),


    path('languages', MovieLanguagesViewSet.as_view({'get': 'list', 'post': 'create'}), name='languages_list'),
    path('languages/<int:pk>/', MovieLanguagesViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                               'delete': 'destroy'}), name='languages_detail'),


    path('moments', MomentsViewSet.as_view({'get': 'list', 'post': 'create'}), name='moments_list'),
    path('moments/<int:pk>/', MomentsViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy'}), name='moments_detail'),


    path('rating', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='rating_detail'),


    path('favorite', FavoriteViewSet.as_view({'get': 'list', 'post': 'create'}), name='favorite_list'),
    path('favorite/<int:pk>/', FavoriteViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                        'delete': 'destroy'}), name='favorite_detail'),


    path('favorite_movie', FavoriteMovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='favorite_movie_list'),
    path('favorite_movie/<int:pk>/', FavoriteMovieViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                                   'delete': 'destroy'}), name='favorite_movie_detail'),


    path('history', HistoryListViewSet.as_view({'get': 'list', 'post': 'create'}), name='history_list'),
    path('history/<int:pk>/', HistoryDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                            'delete': 'destroy'}), name='history_detail'),
]
