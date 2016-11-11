from pagedown.widgets import AdminPagedownWidget
from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Item
        fields = ('title', 'slug', 'pub_date', 'content', 'excerpt', 'thumbnail', 'hero')
