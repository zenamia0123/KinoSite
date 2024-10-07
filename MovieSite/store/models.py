from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(18), MaxValueValidator(100)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    STATUS_CHOICES = (
        ('pro', 'Pro'),
        ('simple', 'Simple'),
    )
    status = models.CharField(max_length=18, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Country(models.Model):
    country_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.country_name


class Director(models.Model):
    director_name = models.CharField(max_length=32)
    country = models.ForeignKey(Country, related_name='directors', on_delete=models.CASCADE)
    bio = models.TextField
    age = models.PositiveSmallIntegerField()
    director_image = models.FileField(upload_to='vid/', verbose_name="Видео", null=True, blank=True)

    def __str__(self):
        return self.director_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=32)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField()
    actor_image = models.FileField(verbose_name="Фото", null=True, blank=True)

    def __str__(self):
        return self.actor_name


class Janre(models.Model):
    janre_name = models.CharField(max_length=35)

    def __str__(self):
        return self.janre_name


class Movie(models.Model):
    movie_name = models.TextField()
    year = models.DateField(auto_now=True)
    country = models.ForeignKey(Country, related_name='movie', on_delete=models.CASCADE)
    director = models.ManyToManyField(UserProfile, blank=True)
    actor = models.ManyToManyField(Actor, verbose_name='актеры', related_name='film_actor')
    janre = models.CharField(max_length=100)
    TYPE_CHOICES = (
        ('144', '144'),
        ('360', '360'),
        ('480', '480'),
        ('720', '720'),
        ('1080', '1080')
    )
    type = models.CharField(max_length=18, choices=TYPE_CHOICES, default='simple')
    movie_time = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    movie_trailer = models.FileField(upload_to='vid/', verbose_name="Видео", null=True, blank=True)
    status_movie = models.CharField(max_length=10, choices=[('pro', 'Pro'), ('simple', 'Simple'), ('480p', '480p')],
                                    default="simple", verbose_name="Статус фильма")

    def __str__(self):
        return self.movie_name

    def get_average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(ratings.stars for rating in ratings) / ratings.count(), 1)
        return 0


class MoviePhotos(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='movie_images/')


class MovieLanguages(models.Model):
    language = models.ForeignKey(Movie, related_name='languages', on_delete=models.CASCADE)
    video = models.ImageField(upload_to='movie_vid/')
    movie = models.ImageField(upload_to='movie_image/')

    def __str__(self):
        return f"{self.language} - {self.video} - {self.movie} movie"


class Moments(models.Model):
   movie = models.ForeignKey(Movie, related_name='moments', on_delete=models.CASCADE)
   movie_moments = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)


class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='ratings', on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(1, str(i)) for i in range(1, 10)], verbose_name='Рейтинг')
    parent_review = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie} - {self.user} - {self.stars} stars'


class Favorite(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='favorite')
    created_date = models.DateTimeField(auto_now_add=True)


class FavoriteMovie(models.Model):
    cart = models.ForeignKey(Favorite, related_name='items', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class History(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.CharField(max_length=32)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} watched {self.movie} on {self.viewed_at}"