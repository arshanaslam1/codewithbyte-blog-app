from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, PostTag, PostCategory, Subscribe



@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'created_on', 'active', 'status',)
    list_filter = ('author', 'category', 'tags', 'created_on', 'hit_count_generic', 'active', 'status',)
    search_fields = ('title', 'category', 'tags',)
    actions = ['approve_posts']

    def approve_posts(self, request, queryset):
        queryset.update(active=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('email',)


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    search_fields = ('title',)


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    search_fields = ('title',)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
