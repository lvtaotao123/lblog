from django.contrib import admin
from blog_index.models import User,Category,Article,Tag,Comment, Indexlink

class ArticleAdmin(admin.ModelAdmin):
    
    class Media:
        js=(
            '/static/lib/kindeditor/kindeditor/kindeditor-all-min.js',
            '/static/lib/kindeditor/kindeditor/lang/zh-CN.js',
            '/static/lib/kindeditor/kindeditor/config.js',
        )

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Indexlink)
# Register your models here.
