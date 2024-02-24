from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from portfolioapp.views import index


urlpatterns = [
    path('kscode/', admin.site.urls),
    path('', index, name='home' )
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)