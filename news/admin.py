from django.contrib import admin
from .models import News, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(Comment)
