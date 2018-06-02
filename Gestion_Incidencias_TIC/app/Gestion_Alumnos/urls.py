from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from app.Gestion_Alumnos.views import Perfil, RegistarAlumno, ListarAlumno, ListarCursoAlumno, RegistarEquipo, \
    ListarEquipoAula, EliminarEquipo, EditarEquipo

urlpatterns = [

    url(r'^perfil/(?P<pk>\d+)/$', Perfil.as_view(), name='perfil'),
    url(r'^registraralumno/$', RegistarAlumno.as_view(), name='registraralumno'),
    url(r'^listaralumno/$', ListarAlumno.as_view(), name='listaralumno'),
    url(r'^alumnocurso/(?P<curso_id>[\w.@+-]+)/$', ListarCursoAlumno.as_view(), name='curso'),
    url(r'^registrarequipo/(?P<aula_id>\d+)/$', RegistarEquipo.as_view(), name='registrarequipo'),
    url(r'^equipoaula/(?P<aula_id>[\w.@+-]+)/$', ListarEquipoAula.as_view(), name='equipoaula'),
    url(r'^eliminarequipo/(?P<pk>[\w.@+-]+)/$', EliminarEquipo.as_view(), name='eliminarequipo'),
    url(r'^editarequipo/(?P<pk>[\w.@+-]+)/$', EditarEquipo.as_view(), name='editarequipo'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)