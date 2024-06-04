from django.urls import path
from . import views
# JE- Trae las urls de la configuración para identificar las imagenes.
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin', views.admin, name='admin'),
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('libros/editar/<int:id>', views.editar, name='editar'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
