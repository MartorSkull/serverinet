# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, timedelta
from . import models

# Create your views here.

def main(request):
    yesterday = date.today() - timedelta(1)
    categoria = models.Categoria.objects.filter(fecha__gt=yesterday)
    return render(request, 'main.html', {'categorias': categoria})

def search(request, search_type):
    if request.method == "POST":
        data = {}
        if search_type == "Competidor":
            barco = request.POST['barco']
            club = request.POST['club']
            data['competidores'] = models.Competidor.objects.filter(club=club, barco=barco)
        elif search_type == "Categoria":
            categoria = request.POST['categoria']
            fecha = request.POST['fecha']
            data['categorias'] = models.Categoria.objects.filter(tipo=categoria, fecha=fecha)
        elif search_type == "Participante":
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            data['participantes'] = models.Participante.objects.filter(nombre=nombre, apellido=apellido)
        return render(request, 'results.html', data)
    return HttpResponse(status=405)

def live(request, categoria_id):
    categoria = models.Categoria.objects.get(id=categoria_id)
    return render(request, 'live.html', {'categoria': categoria})

def live_data(request, categoria_id):
    data = {}
    data['registros'] = models.Registro.objects.filter(competidor__categoria__id=categoria_id).order_by('-hora')
    return render(request, 'live_data.html', data)

def regist(request):
    if request.method == "POST":
        boya = models.Boya.objects.filter(nro=request.POST['nro']).first()
        comp = models.Competidor.objects.filter(id=request.POST['comp']).first()
        new = models.Registro.objects.create(
            boya=boya, 
            competidor=comp, 
            nro_vuelta=request.POST["vuelta"],
            hora=request.POST["tiempo"],
            velocidad=request.POST['velocidad'])
        return HttpResponse(status=200)
    return HttpResponse(status=405)
