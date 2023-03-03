from django.contrib import admin
from .models import NewImagePost, Category, Comment, Status


class NewImagePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'created_time', 'status')
    list_display_links = ('title',)
    actions = ['draft', 'published']

    def draft(self, request, queryset):
        queryset.update(status=Status.Draft)

    def published(self, request, queryset):
        queryset.update(status=Status.Published)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['created_time', 'active']
    list_filter = ['active', 'created_time']
    actions = ['disable_comments', 'activate_comments']

    def disable_comments(self, request, queryset):
        queryset.update(active=False)

    def activate_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(NewImagePost, NewImagePostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
