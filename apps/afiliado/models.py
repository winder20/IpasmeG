# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from ..institucion.models import Institucion


# ---------------------------------- Crea tu Modelo ------------------------------------ #

class Afiliado(models.Model):
	afiliado=models.AutoField(primary_key=True)
	institucion = models.ForeignKey(Institucion)
	cedula_afiliado=models.CharField(max_length=8, unique=True, null=True)
	nombres=models.CharField(max_length=40, null=True)
	apellidos=models.CharField(max_length=40, null=True)
	num_familia=models.CharField(max_length=200, null=True)
	direccion= models.TextField(max_length=500,null=True)
	profecion_afiliado= models.CharField(max_length=200, null=True)
	sitio_traba = models.CharField(max_length=200,null=True)
	ingre_mensu_afiliado = models.CharField(max_length=100,null=True)
	correo= models.EmailField(max_length=100, null=True)
	telefono=models.CharField(max_length=7)
	movil=models.CharField(max_length=7,null=True)
	sector=models.CharField(max_length=50,blank=True)
	comunidad=models.CharField(max_length=50,blank=True)
	avenidad=models.CharField(max_length=50,blank=True)
	calle=models.CharField(max_length=50,blank=True)
	casa=models.CharField(max_length=50,blank=True)
	
	def __unicode__(self):
		return '{} {} {}' .format (self.cedula_afiliado,self.nombres,self.apellidos)
