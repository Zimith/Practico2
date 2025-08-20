from django.db import models
from django.core.exceptions import ValidationError

def Validacion_nombre_corto(value):
    if not value.isupper():
        raise ValidationError(
            f"{value} debe estar en mayúsculas."
        )

class Oficina(models.Model):
    nombre = models.CharField(max_length=50,unique=True)
    nombre_corto = models.CharField(max_length=10,unique=True, help_text="Nombre corto de la oficina (ADM, JAS,MARK, etc)")
    validators = [Validacion_nombre_corto]

    class Meta:
        

        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'

    def __str__(self):
        return f"{self.nombre} - ({self.nombre_corto})"
