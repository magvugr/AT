from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Noticia(models.Model):
	Publicado = 'Publicado'
	Borrador = 'Borrador'

	Titulo = models.CharField(max_length=30)
	Subtitulo = models.CharField(max_length=50)
	Imagen = models.FileField(blank=True, upload_to='media/fotos/noticias')
	SubtituloImag = models.CharField(max_length=30)
	Cuerpo = models.TextField(max_length=500)
	Timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	Actualizado = models.DateTimeField(auto_now_add = False, auto_now = True)
	CHOICES=[(Publicado, 'Publicado'),(Borrador, 'Borrador')]
	Estado = models.CharField(max_length=9,choices=CHOICES, default=Borrador)
	IncluirVideo = models.BooleanField()
	CodVideo = models.CharField(max_length=200)
	Tags = models.CharField(max_length=30)
	usuario = models.ForeignKey(User)

	def __str__(self):
		return self.Titulo + ' - ' + self.Subtitulo

class Evento(models.Model):
	
	Titulo = models.CharField(max_length=30)
	Subtitulo = models.CharField(max_length=50)
	Imagen = models.FileField(blank=True, upload_to='media/fotos/noticias')
	SubtituloImag = models.CharField(max_length=30)
	Cuerpo = models.CharField(max_length=500)
	Timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	Actualizado = models.DateTimeField(auto_now_add = False, auto_now = True)
	Lugar = models.CharField(max_length=50)
	Fecha = models.DateTimeField(auto_now_add = False)
	Organizadores = models.CharField(max_length=30)
	Ponente = models.CharField(max_length=30)
	Tags = models.CharField(max_length=30)

	def __str__(self):
		return self.Titulo + ' - ' + self.Subtitulo