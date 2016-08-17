from django.http import Http404
from .models import Noticia, Evento
from django.shortcuts import render

def index(request):
	todasNoticias = Noticia.objects.all()
	context = {'todasNoticias': todasNoticias}
	return render(request, 'AdiccionTic/index.html', context)

def detalle(request, noticia_id):
	try:
		noticia = Noticia.objects.get(pk=noticia_id)
	except Noticia.DoesNotExist:
		raise Http404("La noticia no existe")
	return render(request, 'AdiccionTic/detalle.html', {'noticia': noticia})

'''
from django.http import HttpResponse

def detalle(request, noticia_id):
	return HttpResponse("<h2> Detalle de la Noticia: " + str(noticia_id) + "</h2>")
'''

'''
#Loader get_template cambio por render
from django.template import loader

def index(request):
	todasNoticias = Noticia.objects.all()
	template = loader.get_template('AdiccionTic/index.html')
	context = {
		'todasNoticias': todasNoticias,
	}
	return HttpResponse(template.render(context, request))
'''

'''
def index(request):
	todasNoticias = Noticia.objects.all()
	html = ''

	for noticia in todasNoticias:
		url = '/adicciontic/' + str(noticia.id) + '/'
		html += '<a href="' + url + '">' + noticia.Titulo + '</a><br>'
	return HttpResponse(html)
'''
