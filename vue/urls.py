from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# from django.conf.urls import url, include
#
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vueapp.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


