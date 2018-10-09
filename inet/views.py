# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from . import models
import json

# Create your views here.

def main(request):
    data = {}
    return render(request, 'main.html', data)

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


def regist(request):
    if request.method == "POST":
        print(request.body)
        data = json.loads(request.body)
        boya = models.Boya.objects.filter(nro=data['boya']).first()
        comp = models.Competidor.objects.filter(id=data['comp']).first()
        new = models.Registro.objects.create(
            boya=boya, 
            competidor=comp, 
            nro_vuelta=data["vuelta"],
            hora=data["tiempo"],
            velocidad=data['velocidad'])
        return HttpResponse(status=200)
    return HttpResponse(status=405)