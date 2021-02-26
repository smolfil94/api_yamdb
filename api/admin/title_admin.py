from django.contrib import admin

from ..models.title import Title


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'description', 'genre', 'category')
    search_fields = ('name',)
    list_filter = ('genre', 'category')


admin.site.register(Title, TitleAdmin)
