from django.conf.urls import url, include
from django.contrib.auth.views import logout_then_login, login


from app.Gestion_Centros import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from app.Gestion_Centros.views import AsignaturasList, Temas, AsignaturasProfesorList, RegistrarTema, RegistrarAula, \
    ListarAulaCurso, RegistrarCursoAula

urlpatterns = [

    url(r'^contacto/', login_required(views.contacto), name='contacto'),
    url(r'^privacidad/', login_required(views.privacidad), name='privacidad'),
    url(r'^inicio/', login_required(views.inicio), name='inicio'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^curso/(?P<curso_id>[\w.@+-]+)/$', AsignaturasList.as_view(), name='curso'),
    url(r'^curso_profesor/(?P<curso_id>[\w.@+-]+)/$', AsignaturasProfesorList.as_view(), name='curso_profesor'),
    url(r'^tema/(?P<asignatura_id>[\w.@+-]+)/(?P<curso_id>[\w.@+-]+)/$', Temas.as_view(), name='tema'),
    url(r'^registrar_tema(?P<curso_id>[\w.@+-]+)/(?P<asignatura_id>[\w.@+-]+)/$', RegistrarTema.as_view(), name='registrar_tema'),
    url(r'^registrar_aula/$', RegistrarAula.as_view(), name='registrar_aula'),
    url(r'^aula_curso/(?P<curso_id>[\w.@+-]+)/$', ListarAulaCurso.as_view(), name='aula_curso'),
    url(r'^registrar_curso_aula/(?P<curso_id>[\w.@+-]+)/$', RegistrarCursoAula.as_view(), name='registrar_curso_aula'),

    #url(r'^tema/(?P<asignatura_id>[\w.@+-]+)/$', Temas.as_view(), name='tema'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
