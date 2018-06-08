"""Gestion_Incidencias_TIC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete, password_change, password_change_done

urlpatterns = [
    url(r'^$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^alumno/', include('app.Gestion_Alumnos.urls', namespace='alumno')),
    url(r'^centro/', include('app.Gestion_Centros.urls', namespace='centro')),
    url(r'^calendar/', include('calendarium.urls')),
    url(r'^solicitud/', include('app.Gestion_Solicitudes.urls', namespace='solicitud')),
    url(r'^profesor/', include('app.Gestion_Profesores.urls', namespace='profesor')),
    url(r'^$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^reset/password_reset', password_reset, {'template_name': 'registration/password_reset_form.html', 'template_name':'registration/password_reset_form.html'}, name='password_reset'),
    url(r'^reset/password_reset_done', password_reset_done, {'template_name': 'registration/password_reset_done.html', 'template_name':'registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {'template_name': 'registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^password_change', password_change, {'template_name': 'registration/password_change_form.html', 'template_name': 'registration/password_change_form.html'},name='password_change'),
    url(r'^password_change_done', password_change_done, {'template_name': 'registration/password_change_done.html'},name='password_change_done'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Gestion Incidencias TIC"
admin.site.index_title = "Panel de administrador"