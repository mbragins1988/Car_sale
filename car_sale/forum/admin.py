from django.contrib import admin
from forum.models import Forum


class ForumAdmin(admin.ModelAdmin):
    pass


admin.site.register(Forum, ForumAdmin)
