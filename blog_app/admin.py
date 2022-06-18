from django.contrib import admin
from .models import Post
# Register your models here.
class BlogDB(admin.ModelAdmin):
    list_display = [
        "title","text","author","created_date","published_date"
    ]


admin.site.register(Post, BlogDB)
