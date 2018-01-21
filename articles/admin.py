from django.contrib import admin
from .models import Articles

# Register your models here.


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'author']
    list_filter = ['created']
    search_fields = ['title', 'description', 'content']
    date_hierarchy = 'created'
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Articles, ArticlesAdmin)
