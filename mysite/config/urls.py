from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from projects.views import index, projects, get_all_posts

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'projects/(?P<slug>[-\w]+)/$', projects, name="projects"),
    url(r'^api/posts/$', get_all_posts),
]

if settings.DEBUG is True:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
