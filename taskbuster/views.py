# -*- coding: utf-8 -*-
import datetime
from django.shortcuts import render
from django.utils.timezone import now

def home(request):
    today = datetime.date.today()
    return render(request, "taskbuster/index.html", 
        {'today': today, 'now': now})

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

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")

