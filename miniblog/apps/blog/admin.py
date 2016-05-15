from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    fieldsets = (
        (u'General', {
            'fields' : ('title',)
        }),
        (u'Content', {
            'fields' : ('content',)
        }),
        (u'Date and Time', {
            'fields' : ('created_date', 'updated_date')
        }),
    )

    list_display = ('title', 'content', 'created_date', 'updated_date')
    list_filter = ('created_date', 'updated_date')
    search_fields = ('title',)
    ordering = ('title',)
    readonly_fields = ('created_date', 'updated_date')

admin.site.register(Blog, BlogAdmin)
admin.site.unregister(Group)
