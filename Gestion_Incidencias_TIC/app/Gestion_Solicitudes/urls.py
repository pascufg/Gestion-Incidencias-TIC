from django.conf.urls import url

from app.Gestion_Solicitudes import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from app.Gestion_Solicitudes import views as solicitudes_views
from app.Gestion_Solicitudes.views import EliminarSolicitud, EditarSolicitud

urlpatterns = [

    url(r'^registrarsolicitud/', views.SolicitudCreate.as_view(), name='registrarsolicitud'),
    url(r'^listarsolicitud/', login_required(solicitudes_views.listarSolicitud), name='listarsolicitud'),
    url(r'^search/', solicitudes_views.search, name='search'),
    url(r'^eliminar_solicitud/(?P<pk>\d+)/$', EliminarSolicitud.as_view(), name="eliminar_solicitud"),
    url(r'^editarsolicitud/(?P<pk>\d+)/$', EditarSolicitud.as_view(), name="editarsolicitud"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

