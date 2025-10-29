from django.contrib import admin
from . import models

def publish_posts(modeladmin, request, queryset):
    queryset.update(is_published=True)
publish_posts.short_description = "Publish selected posts"

def unpublish_posts(modeladmin, request, queryset):
    queryset.update(is_published=False)
unpublish_posts.short_description = "Unpublish selected posts"


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']

class CommentInline(admin.StackedInline):
    model = models.Comment
    extra = 1

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_published', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'title']
    date_hierarchy = 'created_at'
    actions = [publish_posts, unpublish_posts]
    inlines = [CommentInline]

@admin.register(models.Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['comment', 'post', 'author', 'created_at']
    search_fields = ['comment', 'post', 'author']
    list_filter = ['created_at']
    date_hierarchy = 'created_at'