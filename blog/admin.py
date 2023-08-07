from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on', 'category')
    search_fields = ['title', 'content', 'category']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'category')
    summernote_fields = ('content')
