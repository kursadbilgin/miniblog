from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    fieldsets = (
        (u'General', {
            'fields' : ('title',)
        }),
        (u'Content and Status', {
            'fields' : ('is_important', 'content')
        }),
        (u'Date and Time', {
            'fields' : ('created_date', 'updated_date')
        }),
    )

    list_display = ('title', 'created_date', 'updated_date', 'is_important')
    list_filter = ('is_important', 'created_date', 'updated_date')
    search_fields = ('title',)
    ordering = ('title',)
    readonly_fields = ('created_date', 'updated_date')


admin.site.register(Blog, BlogAdmin)
admin.site.unregister(Group)
