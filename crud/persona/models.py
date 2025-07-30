from django.db import models

class Persona(models.Model):
    """Model definition for MODELNAME."""
    apellido = models.CharField(verbose_name="apellido", max_length=50)
    nombre = models.CharField(verbose_name="nombre", max_length=50)
    edad = models.IntegerField(verbose_name="edad")

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return f"{self.apellido} - {self.nombre} {self.edad}"

