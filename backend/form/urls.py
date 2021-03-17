from rest_framework import generics
from django.contrib import admin
from django.urls import path
from .views import complaintView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
	path('postdata/',complaintView),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

