from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=50)
    subjects = models.TextField(blank=True)
    bookshelves = models.TextField(blank=True)
    download_links = models.JSONField(default=list)
    popularity = models.PositiveIntegerField(default=0)
    book_id = models.PositiveIntegerField(blank=True, null=True)
    mime_type = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
