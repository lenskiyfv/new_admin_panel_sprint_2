from django.contrib import admin

from .models import Genre, Person, Filmwork, GenreFilmwork, PersonFilmwork


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork


class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Filmwork)
class FilmWorkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline, PersonFilmworkInline,)
    list_display = ('title', 'type', 'creation_date', 'rating',)
    list_filter = ('type', 'creation_date', 'rating',)
