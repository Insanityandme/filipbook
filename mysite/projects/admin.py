from pagedown.widgets import AdminPagedownWidget

from django.db import models
from django.contrib import admin

from mysite.projects.models import Item, ItemImage, Category, ContentType


# Register your models here.
class ItemImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'item',)


class ItemImageInline(admin.StackedInline):
    model = ItemImage


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date',)
    list_filter = ('pub_date',)
    ordering = ('-pub_date',)
    search_fields = ('title',)

    inlines = [ItemImageInline, ]

    formfield_overrides = {
            models.TextField: {'widget': AdminPagedownWidget},
    }


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ContentTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle',)


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemImage, ItemImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ContentType, ContentTypeAdmin)
