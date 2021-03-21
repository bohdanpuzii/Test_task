from django.contrib import admin
from .models import Post, Comment

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Comment)


from django.urls import path, reverse
from django.shortcuts import redirect
from django.utils.html import format_html


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'photo', 'author', 'approve_button')

    @staticmethod
    def approve_button(self):
        return format_html(
            f'<a class="button" href="{reverse("admin:delete_comments", args=[self.id])}">Delete comments</a>')

    def get_urls(self):
        urls = super().get_urls()
        shard_urls = [path('delete_comments/<int:post_id>', self.admin_site.admin_view(self.delete_comments),
                           name="delete_comments"), ]
        # Список отображаемых столбцов
        return shard_urls + urls

    @staticmethod
    def delete_comments(self, post_id):
        comments_to_delete = Comment.objects.filter(post=post_id)
        comments_to_delete.delete()
        return redirect(reverse('admin:main_post_changelist'))
