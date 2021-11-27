from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from hesap import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index, name='index'),
                  path('kayit/', views.kayit, name='kayit'),
                  path('goster/<int:pk>/', views.goster, name='goster'),
                  path('cv/<int:pk>/', views.pdf_generate, name='cv'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
