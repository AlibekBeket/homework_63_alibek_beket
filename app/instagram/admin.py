from django.contrib import admin

from instagram.models import Posts, Comments


# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "img", "description", "likes", "comments")
    list_filter = ("id", "user", "description", "likes", "comments")
    search_fields = ("id", "user", "description", "likes", "comments")
    fields = ("user", "description", "img", "likes", "comments")
    readonly_fields = ("id",)


admin.site.register(Posts, PostsAdmin)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "description", "post", "likes")
    list_filter = ("id", "user", "description", "post", "likes")
    search_fields = ("id", "user", "description", "post", "likes")
    fields = ("user", "description", "post", "likes")
    readonly_fields = ("id",)


admin.site.register(Comments, CommentsAdmin)