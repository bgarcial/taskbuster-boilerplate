# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import TemplateView


def home(request):
    return render(request, "taskbuster/index.html", {})

"""
El shortcut render me permite cargar un template, 
crear un contexto adicionando un conjunto de variables
por defecto, tales como info acerca del actual user logueado
o el actual lenguaje del sitio.
Es decir renderea todo esto en la plantilla y devuelve un
http response, todo en una funcion

Note: the information added by default depends on 
the template context processors that you have included 
in your settings file.
"""    

#class HomeView(TemplateView):
#    template_name = 'index.html'