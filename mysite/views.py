import json
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.http import HttpResponse
from mysite.projects.serializers import ItemSerializer
from mysite.projects.models import Item


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


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
    serializer = ItemSerializer(items, many=True)

    return JSONResponse(serializer.data)
