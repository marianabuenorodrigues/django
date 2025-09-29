from django.contrib import admin
from .models import Post

@admin.register(Post)
class Post(admin.ModelAdmin)    :
    list_display = ('title', 'author', 'created_date', 'published_date')
    # list_filter = ('published_date', 'author')
    # search_fields = ('title', 'text')
    # date_hierarchy = 'published_date'
    # ordering = ('published_date',)  

