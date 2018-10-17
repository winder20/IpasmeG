# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


# Crea tu Vista Aqui.

def inicio(request):
	return render(request ,"base/index.html")


def sobre_nosotros(request):
	return render(request ,"base/about-us.html")

def galeria(request):
	return render(request ,"base/portfolio.html")


def blog(request):
	return render(request ,"base/blog.html")


def contacto(request):
	return render(request ,"base/contact-us.html")