from django.contrib import admin
from .models import Post, Comment, Category, Profile
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Category)

admin.site.register(Profile)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Filters and display fields for Posts on admin panel
    """

    list_display = ('title', 'slug', 'status', 'created_on', 'category')
    search_fields = ['title', 'content', 'category']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'category')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Filters and display fields for Comments on admin panel

    Approve comments method to allow all comments to be approved
    by an admin before they appear on the website.
    """

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
