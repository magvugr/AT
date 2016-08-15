from django.http import HttpResponse
from django.template import loader
from .models import Noticia, Evento

def index(request):
	todasNoticias = Noticia.objects.all()
	template = loader.get_template('AdiccionTic/index.html')
	context = {
		'todasNoticias': todasNoticias,
	}
	return HttpResponse(template.render(context, request))

'''
def index(request):
	todasNoticias = Noticia.objects.all()
	html = ''

	for noticia in todasNoticias:
		url = '/adicciontic/' + str(noticia.id) + '/'
		html += '<a href="' + url + '">' + noticia.Titulo + '</a><br>'
	return HttpResponse(html)
'''
def detalle(request, noticia_id):
	return HttpResponse("<h2> Detalle de la Noticia: " + str(noticia_id) + "</h2>")
