# -*- coding: utf-8 -*-

# -------------------------------- Aqui se Importan tus Modelos --------------------------------- #


from __future__ import unicode_literals
from django.contrib import admin
from ..reposo.models import Reposo

# --------------------------------- Registra tu modelo aqui ------------------------------------ #

admin.site.register(Reposo)