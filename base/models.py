from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Cada clase que creemos dentro de models es una tabla y sus atributos son sus columnas

# 1 tabla
class Tarea(models.Model):
    # clave externa para poder relacionarlo con tareas
    usuario = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    # CharField (cadena caracteres)
    titulo = models.CharField(max_length=100)

    descripcion = models.TextField(null=True,
                                   blank=True)

    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    # Al imprimirse una tarea, se imprime el titulo
    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['completo'] # El campo completo marca el orden.

