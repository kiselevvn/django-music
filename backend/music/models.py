from django.db import models


class Genre(models.Model):
    name = models.CharField(
        verbose_name="Наименование жанра",
        max_length=100
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Artist(models.Model):
    scene_name = models.CharField(
        verbose_name="Сценическое имя исполнителя",
        max_length=250
    )
    name = models.CharField(
        verbose_name="Имя исполнителя",
        max_length=250,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"

    def __str__(self):
        if self.name:
            return f"{self.scene_name} ({self.name})"
        return self.scene_name


class Album(models.Model):
    artists = models.ManyToManyField(
        Artist,
        verbose_name="Исполнитель",
        null=True,
        blank=True
    )
    genre = models.ForeignKey(
        Genre,
        verbose_name="Жанр",
        on_delete=models.CASCADE,
        related_name="albums",
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование альбома",
    )
    release_date = models.DateField(verbose_name="Дата релиза")

    class Meta:
        ordering = ["name", "release_date"]
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

    def __str__(self):
        return self.name


class Track(models.Model):
    album = models.ForeignKey(
        Album,
        verbose_name="Альбом",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Трэк"
        verbose_name_plural = "Трэки"

    def __str__(self):
        return self.name