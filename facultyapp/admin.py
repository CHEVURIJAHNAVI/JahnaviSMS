from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')  # Show title and publication date in admin
    prepopulated_fields = {"slug": ("title",)}  # Slug is prepopulated from the title

admin.site.register(BlogPost, BlogPostAdmin)
from django.contrib import admin

# Register your models here.
