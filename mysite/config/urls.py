from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from projects.views import index, projects, get_all_posts, get_all_categories

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'projects/(?P<url>[-\w]+)/$', projects),
    url(r'^api/posts/$', get_all_posts),
    url(r'^api/categories/$', get_all_categories),
]

if settings.DEBUG is True:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
