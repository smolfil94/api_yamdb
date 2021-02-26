from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .title import Title

User = get_user_model()


class Review(models.Model):
    text = models.TextField()
    score = models.PositiveIntegerField(validators=[
                                            MinValueValidator(1),
                                            MaxValueValidator(10)
                                        ],
                                        verbose_name='Оценка'
                                        )
    title = models.ForeignKey(Title,
                              on_delete=models.CASCADE,
                              related_name='reviews',
                              blank=True,
                              verbose_name='Название произведения')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='reviews',
                               verbose_name='Автор')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')

    class Meta:
        ordering = ['-pub_date']
