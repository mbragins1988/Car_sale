from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('car/', include('car.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

handler404 = 'car.views.page_not_found'
handler403 = 'car.views.permission_denied'
handler500 = 'car.views.server_error'
