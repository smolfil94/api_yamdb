from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator 
from .title import Title


User = get_user_model()

class Review(models.Model):
    text = models.TextField()
    score = models.PositiveIntegerField(default=None, 
                                        validators=[
                                            MinValueValidator(1), 
                                            MaxValueValidator(10)
                                            ])
    title = models.ForeignKey(Title, 
                                 on_delete=models.CASCADE, 
                                 related_name='reviews',
                                 blank=True)
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE,
                               related_name='reviews')
    pub_date = models.DateTimeField('Дата публикации', 
                                    auto_now_add=True)
    
    class Meta:
        ordering = ['-pub_date',]



