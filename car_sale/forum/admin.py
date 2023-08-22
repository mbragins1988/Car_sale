from django.contrib import admin
from forum.models import *


class ForumAdmin(admin.ModelAdmin):
    pass

class Category_forumAdmin(admin.ModelAdmin):
    pass


admin.site.register(Forum, ForumAdmin)
admin.site.register(Category_forum, ForumAdmin)
