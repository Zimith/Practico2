from django.db import models
from oficina.models import Oficina

class Persona(models.Model):
    """Model definition for MODELNAME."""
    apellido = models.CharField(verbose_name="apellido", max_length=50)
    nombre = models.CharField(verbose_name="nombre", max_length=50)
    edad = models.IntegerField(verbose_name="edad")
    oficina = models.ForeignKey(Oficina, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return f"Nombre Completo: {self.nombre} {self.apellido} - Edad: {self.edad}"

