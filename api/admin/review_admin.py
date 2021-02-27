from django.contrib import admin

from ..models.review import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'score', 'title', 'author', 'pub_date')


admin.site.register(Review, ReviewAdmin)
