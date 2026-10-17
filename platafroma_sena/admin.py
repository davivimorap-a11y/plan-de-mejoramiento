
from django.contrib import admin
from .models import Sede, AmbienteFormacion, Instructor


@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre')
    search_fields = ('codigo', 'nombre')
    ordering = ('nombre',)


@admin.register(AmbienteFormacion)
class AmbienteFormacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_aula', 'capacidad_maxima', 'sede')
    search_fields = ('codigo_aula', 'sede__nombre')
    list_filter = ('sede',)
    ordering = ('codigo_aula',)


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'documento',
        'nombres',
        'apellidos',
        'correo_institucional'
    )
    search_fields = ('documento', 'nombres', 'apellidos', 'correo_institucional')
    ordering = ('apellidos', 'nombres')
    filter_horizontal = ('ambientes',)
