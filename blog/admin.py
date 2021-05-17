from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'publish')
    list_filter = ('status', 'publish', 'create')
    search_fields = ('title', 'body')
    ordering = ('status', 'publish')
    date_hierarchy = 'publish'   # daste  bandi tarikh postha
    prepopulated_fields = {'slug':('title',)} # slug khodkat
    raw_id_fields = ('author',)    #author bar asas id sabt mikoni



