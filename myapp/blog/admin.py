from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_filter = ('created_at', 'category')
    search_fields = ('title', 'content')
class CategoryField(admin.ModelAdmin):
    search_fields = ('created_at', 'post')  
admin.site.register(Post, PostAdmin)
admin.site.register(Category)