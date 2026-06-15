from django.contrib import admin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    search_fields = ('title', 'author__username',
                     'author__first_name', 'categories__name')
    date_hierarchy = "published"
    list_filter = ('title', 'author__first_name', 'published', )
    list_display = ('title', 'author__first_name',
                    'published', 'categories_names', )

    def author_name(self, obj):
        return obj.author.first_name

    def categories_names(self, obj):
        # res = ''
        # for category in obj.categories.all().order_by("name"):
        #     res += category.name + ", "
        # return res[:-2]
        return ", ".join([category.name for category in obj.categories.all().order_by("name")])
    categories_names.short_description = 'Categorías'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
