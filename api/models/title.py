from django.db import models

from .category import Category
from .genre import Genre


class Title(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    genre = models.ManyToManyField(Genre, related_name='titles',)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True,
                                 related_name='titles',)

    class Meta:
        ordering = ['name']
