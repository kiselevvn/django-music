from django.contrib import admin
from .models import Artist, Track, Album, Genre
from django.utils.http import urlencode
from django.urls import reverse
from django.utils.html import format_html


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        "scene_name",
        "name",
        "id",
    )
    search_fields = ("name", "scene_name",)


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )
    search_fields = ("name",)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "release_date",
        "genre",
        "id",
    )
    list_filter = (
        "genre",
    )
    search_fields = ("name",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "genre_link",
        "id",
    )

    def genre_link(self, obj):
        count = obj.albums.count()

        if count == 0:
            return format_html('<span style="color:red;">Нет альбомов</span>')

        url = (
                reverse("admin:music_album_changelist")
                + "?"
                + urlencode({"genre__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">Открыть {}</a>', url, count)

    genre_link.short_description = "Альбомы жанра"
