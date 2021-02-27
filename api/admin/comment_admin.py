from django.contrib import admin

from ..models.comment import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'text', 'author', 'pub_date')


admin.site.register(Comment, CommentAdmin)
