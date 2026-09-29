from django.contrib import admin

# Register your models here.
from .models import Post

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'is_featured', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('status', 'is_featured')
    ordering = ('-created_at',)