from django.conf.urls import url
from django.contrib import admin

# For development
from django.conf import settings
from django.conf.urls.static import static

from projects.views import index, get_all_posts, get_item_content_by_url, get_all_categories

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^api/posts/$', get_all_posts),
    url(r'^api/categories/$', get_all_categories),
    url(r'^api/posts/(?P<url>[-\w]+)/$', get_item_content_by_url),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
