from django.conf.urls import url
from django.contrib import admin

# For development
from django.conf import settings
from django.conf.urls.static import static

from mysite.views import index, get_all_posts, get_item_content_by_link

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^api/posts/$', get_all_posts),
    url(r'^api/posts/(?P<link>[-\w]+)/$', get_item_content_by_link),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
