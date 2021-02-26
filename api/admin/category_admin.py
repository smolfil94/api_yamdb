from django.contrib import admin

from ..models.category import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


admin.site.register(Category, CategoryAdmin)
