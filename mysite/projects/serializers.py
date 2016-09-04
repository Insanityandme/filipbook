from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Item
        exclude = ('content',)
        depth = 2

    def get_thumbnail(self, obj):
        return obj.thumbnail.url
