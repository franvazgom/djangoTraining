from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.urls import core_urlpatterns
from blog.urls import blog_urlpatterns
from pages.urls import pages_urlpatterns


urlpatterns = [
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('admin/', admin.site.urls),
    path('', include(core_urlpatterns)),
    path('blog/', include(blog_urlpatterns)),
    path('pages/', include(pages_urlpatterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
