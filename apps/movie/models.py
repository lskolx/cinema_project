from django.db import models
from apps.genre.models import Genre
from django.contrib.auth import get_user_model
from slugify import slugify


User = get_user_model()

class Film(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_pub', verbose_name='Author')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    content = models.TextField()
    year = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='film_genre', null=True)
    country = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='Images', default="Images/81KoSSAwH2L._SL1500_.jpg")


    def __str__(self) -> str:
        return f'{self.title} from {self.year}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Film, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-year']

class FilmImage(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='film_images')
    image = models.ImageField(upload_to='film_images')

    def __str__(self) -> str:
        return self.film


class Favorites(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return str(self.like)