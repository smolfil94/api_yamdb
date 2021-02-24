from django.contrib.auth import get_user_model
from django.db import models

from .review import Review

User = get_user_model()


class Comment(models.Model):
    text = models.TextField()
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name='comments')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments')
    pub_date = models.DateTimeField('Дата публикации',
                                    auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
