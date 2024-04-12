from django.db import models


# Create your models here.

class Author(models.Model):
    author = models.CharField(max_length=256, null=True, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='authors',
        null=True,
        blank=True,
    )
