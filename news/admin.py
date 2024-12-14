from django.contrib import admin
from django.utils.safestring import mark_safe


from .models import Post, Category

# Register your models here.


admin.site.register(Category)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'updated', 'views', 'category', 'published', 'get_photo')
    list_display_links = ('id', 'title')
    list_editable = ('category', 'published')
    list_filter = ('category', 'published')
    search_fields = ('title', 'content')
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = False
    save_on_top = False
    readonly_fields = ('views',)

    def get_photo(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" width="150px">')
        return "-"

    get_photo.short_description = "Rasmi"



admin.site.register(Post, PostAdmin)