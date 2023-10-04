from django.contrib import admin

from .models import Estudante,Curso,Nota

admin.site.register(Estudante)
admin.site.register(Curso)
admin.site.register(Nota)

