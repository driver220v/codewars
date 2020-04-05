from django.contrib import admin

from .models import BD


# Register your models here.
class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'date_posted')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(BD, BdAdmin)
