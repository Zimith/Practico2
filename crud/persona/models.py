from django.db import models
from oficina.models import Oficina
from django.core.validators import MinValueValidator, MaxValueValidator

class Persona(models.Model):
    """Model definition for MODELNAME."""
    apellido = models.CharField(verbose_name="apellido", max_length=50)
    nombre = models.CharField(verbose_name="nombre", max_length=50)
    edad = models.IntegerField(verbose_name="edad",
    validators=[
        MinValueValidator(18, message="La edad mínima es 18 años."),
        MaxValueValidator(90, message="La edad máxima es 90 años.")
    ],
    help_text="Ingrese la edad de la persona.")
    oficina = models.ForeignKey(Oficina, on_delete=models.PROTECT, related_name="personas", null=True, blank=True)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        """Unicode representation of Persona."""
        oficina_str = self.oficina.nombre_corto if self.oficina else "Sin oficina"
        return f"{self.apellido}, {self.nombre} (Edad: {self.edad}) - Oficina: {oficina_str}"

