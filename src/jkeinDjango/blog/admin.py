from django.contrib import admin
from models import Category, Article
from tinymce.widgets import TinyMCE
from django.db import models

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {models.TextField: {'widget': TinyMCE(attrs={'cols': 60, 'rows': 20},)},}
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"name_slug": ("name",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)