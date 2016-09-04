import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mysite.projects.models import Item

# Extend HttpResponse with your own JSONresponse instead of repeating code.


def index(request):
    return render(request, 'index.html', {})


def get_item_content_by_link(request, link):
    # returns a list()
    content = Item.objects.filter(link=link).values('content')
    # returns a json object
    content = json.dumps(content[0])
    return HttpResponse(content, content_type="application/json")


def get_all_posts(request):
    items = Item.objects.all().defer('content')
    items = serializers.serialize("json", items, use_natural_foreign_keys=True)

    return HttpResponse(items, content_type="application/json")
