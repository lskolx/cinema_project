# Generated by Django 4.0.5 on 2022-07-03 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genre', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('content', models.TextField()),
                ('year', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default='Images/81KoSSAwH2L._SL1500_.jpg', null=True, upload_to='Images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_pub', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='film_genre', to='genre.genre')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'ordering': ['-year'],
            },
        ),
        migrations.CreateModel(
            name='FilmImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='film_images')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_images', to='movie.film')),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_favorite', models.BooleanField(default=False)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='movie.film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
