# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Categoria(models.Model):
    tipo = models.CharField(max_length=30)
    fecha = models.DateField()

    def __str__(self):
        return "{}".format(self.tipo)

class Boya(models.Model):
    nro = models.IntegerField()
    km = models.IntegerField()
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE,
        related_name="boyas",
        related_query_name="boya"
    )

    def __str__(self):
        return "Boya {}".format(self.nro)

class Competidor(models.Model):
    barco = models.CharField(max_length=30)
    club = models.CharField(max_length=30)
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE,
        related_name="competidores",
        related_query_name="competidor"
    )

    def __str__(self):
        return "categoria: {}, barco: {}".format(self.categoria, self.barco)

class Participante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    competencia = models.ForeignKey(
        Competidor, 
        on_delete=models.CASCADE,
        related_name="participantes",
        related_query_name="participante"
    )

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)

class Registro(models.Model):
    boya = models.ForeignKey(
        Boya, 
        on_delete=models.CASCADE,
        related_name="registros",
        related_query_name="registro",
        null=True,
        blank=True
    )
    competidor = models.ForeignKey(
        Competidor, 
        on_delete=models.CASCADE,
        related_name="registros",
        related_query_name="registro"
    )
    nro_vuelta = models.IntegerField()
    hora = models.TimeField()
    velocidad = models.FloatField()

    def __str__(self):
        return "hora: {}".format(self.hora)
    """
    def tiempo(self):   
        last = Registro.objects.filter(hora__lte=self.hora, competidor = self.competidor).order_by('hora').last()
        if last:
            dif = self.hora - last.hora 
            return dif
        return 0
    """