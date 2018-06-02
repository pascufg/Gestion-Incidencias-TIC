from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from app.Gestion_Profesores.views import ListarCursoProfesor, ListarCursoAsignaturaProfesor

urlpatterns = [
    url(r'^curso/(?P<profesor_id>[\w.@+-]+)/$', ListarCursoProfesor.as_view(), name='curso'),
    url(r'^curso_aula/(?P<profesor_id>[\w.@+-]+)/$', ListarCursoAsignaturaProfesor.as_view(), name='curso_aula'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)