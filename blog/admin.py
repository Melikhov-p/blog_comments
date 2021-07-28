from django.contrib import admin

from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'date')
    search_fields = ('title', 'content',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'article', 'parent_com')
    search_fields = ('user',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)