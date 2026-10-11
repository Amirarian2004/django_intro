from django.contrib import admin

from .models import Category, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'is_featured', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('status', 'is_featured')
    ordering = ('-created_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)