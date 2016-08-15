
from django.conf.urls import url
from . import views

urlpatterns = [
	#/adicciontic/
    url(r'^$', views.index, name='index'),

    #/adicciontic/1
    url(r'^(?P<noticia_id>[0-9]+)/$', views.detalle, name='detalle'),
]
