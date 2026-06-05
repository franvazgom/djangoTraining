from django.contrib import admin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_display = ('title', 'author_name', 'published')
    search_fields = ('title', 'author__username', 'author__first_name', 'categories__name')

    def author_name(self, obj):
        return obj.author.first_name


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
