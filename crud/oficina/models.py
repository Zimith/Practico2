from django.db import models

class Oficina(models.Model):
    nombre = models.CharField(max_length=50)
    nombre_corto = models.CharField(max_length=50)

    class Meta:
        

        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'

    def __str__(self):
        return f"{self.nombre} - ({self.nombre_corto})"
