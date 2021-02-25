from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='category')
    slug = models.SlugField(unique=True, verbose_name='slug')

    class Meta:
        ordering = ['name']
