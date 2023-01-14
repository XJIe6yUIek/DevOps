from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path('demand', views.demand),
    path('geography', views.geography),
    path('skills', views.skills),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)