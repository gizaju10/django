from django.contrib import admin

from blog.models import Category, Tag, Post, ContentImage, Comment, Reply

# ブログの本文中に画像を挿入
class ContentImageInline(admin.TabularInline):
    model = ContentImage
    extra = 1

# ブログの本文中に画像を挿入
class PostAdmin(admin.ModelAdmin):
    inlines = [
        ContentImageInline,
    ]


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Reply)