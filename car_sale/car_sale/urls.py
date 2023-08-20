from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include('car.urls', namespace='car')),
    path('forum/', include('forum.urls', namespace='forum')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

handler404 = 'car.views.page_not_found'
handler403 = 'car.views.permission_denied'
handler500 = 'car.views.server_error'
