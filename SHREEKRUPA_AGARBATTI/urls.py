from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('why-are-you-finding-this-page/', admin.site.urls),
    path('project-design/', include('ProjectDesign.urls', namespace='ProjectDesign')),
    path('project-model/', include('ProjectModel.urls', namespace='ProjectModel')),
    path('project-real/', include('ProjectReal.urls', namespace='ProjectReal')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
