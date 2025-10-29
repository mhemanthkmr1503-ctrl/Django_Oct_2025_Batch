from django.contrib import admin
from . import models

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'title']
    date_hierarchy = 'created_at'