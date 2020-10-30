from django.contrib import admin
from .models import Post,Comment
# Register your models here.
class CommentInline(admin.TabularInline): #StackedInline hiển thị comment theo hàng dọc
    model  = Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_filter = ['created']
    search_fields = ['title']
    inlines = [CommentInline]
admin.site.register(Post,PostAdmin)
