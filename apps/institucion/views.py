# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


# Crea tu Vista Aqui.

def index3(request):
	 return HttpResponse('Institucion')