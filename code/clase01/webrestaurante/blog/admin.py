from django.contrib import admin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('title', 'author_name', 'published',)
    search_fields = ('title', 'categories__name', 'author__first_name',)
    date_hierarchy = 'published'

    def author_name(self, obj):
        return obj.author.first_name + " " + obj.author.last_name


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
