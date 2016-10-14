# from pagedown.widgets import AdminPagedownWidget

# from django.db import models
from .forms import ItemForm
from django.contrib import admin

from .models import Item, ItemImage


# Register your models here.
class ItemImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'item',)


class ItemImageInline(admin.StackedInline):
    model = ItemImage


class ItemAdmin(admin.ModelAdmin):
    form = ItemForm
    list_display = ('title', 'pub_date', )
    list_filter = ('pub_date',)
    ordering = ('-pub_date',)
    search_fields = ('title',)

    inlines = [ItemImageInline, ]

    # formfield_overrides = {
    # models.TextField: {'widget': AdminPagedownWidget},
    # }

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemImage, ItemImageAdmin)
