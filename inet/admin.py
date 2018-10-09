# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Boya)
admin.site.register(models.Categoria)
admin.site.register(models.Competidor)
admin.site.register(models.Participante)
admin.site.register(models.Registro)

