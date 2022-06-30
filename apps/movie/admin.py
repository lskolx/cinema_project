from django.contrib import admin
from .models import Film, FilmImage
from django.contrib import admin
from django.utils.safestring import mark_safe


# class FilmImageAdmin(admin.TabularInline):
#     model = FilmImage
#     extra = 1


# @admin.register(Film)
# class FilmAdmin(admin.ModelAdmin):
#     model = Film
#     list_display = ('title', 'slug', 'year', 'views_count', 'genre', 'country', )
#     prepopulated_fields = {'slug': ('title', )}
#     inlines = [FilmImageAdmin]


class InlineFilmImage(admin.TabularInline):
    model = FilmImage
    extra = 1
    fields = ('image',)


class FilmAdmin(admin.ModelAdmin):
    model = Film
    list_display = ('title', 'slug', 'year', 'genre', 'country', 'image', )
    prepopulated_fields = {'slug': ('title', )}
    inlines = [InlineFilmImage, ]
    list_filter = ('genre', 'country', )

    def image(self, obj):
        img = obj.image.first()
        if img:
            return mark_safe(f"<img scr='{img.image.url}' width='80' height='80' style='object-fit: contain'/>")
        else:
            return ""


admin.site.register(Film, FilmAdmin)