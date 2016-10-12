from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Item, Category


def index(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'index.html', context)


def projects(request, url):
    # returns a list()
    # content = Item.objects.filter(url=url).values('content')
    context = {}
    # returns a json object
    return render(request, 'projects/projects.html', context)


def get_all_posts(request):
    items = Item.objects.all().defer('content')
    items = serializers.serialize("json", items, use_natural_foreign_keys=True)

    return HttpResponse(items, content_type="application/json")


def get_all_categories(request):
    categories = Category.object.all()

    categories = serializers.serialize("json", categories)

    return HttpResponse(categories, content_type="application/json")
