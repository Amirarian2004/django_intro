from django.contrib import admin

from .models import Category, Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'is_featured', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('status', 'is_featured', 'category', 'tags')
    ordering = ('-created_at',)
    filter_horizontal = ('tags',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)