from django.contrib.auth import get_user_model
from django.db import models

from .review import Review

User = get_user_model()


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст')
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='Отзыв')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='Автор')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации',
                                    db_index=True)

    class Meta:
        ordering = ['-pub_date']
