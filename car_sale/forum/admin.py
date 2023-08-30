from django.contrib import admin
from forum.models import *


class ForumAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'slug', 'time_create', 'text', 'is_published'
        )
    list_display_links = ('id', 'title', 'slug')
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

class Category_forumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Forum, ForumAdmin)
admin.site.register(Category_forum, Category_forumAdmin)
