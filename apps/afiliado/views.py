# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from django.core.urlresolvers import reverse_lazy
#from .forms import *
from .models import *


# Crea tu Vista Aqui.

def Afiliado(request):
	if request.method == 'POST':
		form = AfiliadoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('afiliado:index')
	else: 
		form = AfiliadoForm()
	return render(request,'afiliado/afiliado.html',{'form':form})





