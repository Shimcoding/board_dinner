
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acc/',include('acc.urls')),
    path('board/',include('board.urls')),
    path('vote/',include('vote.urls')),
    path('trans/',include('trans.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
