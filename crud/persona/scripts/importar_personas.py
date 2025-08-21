import csv
import sys
from django.db import transaction
from django.core.exceptions import ValidationError
from persona.models import Persona
from oficina.models import Oficina
def run(*args):
    if not args:
        print("Error: Favor de proporcionar la ruta del archivo")
        print("Uso: ./manage.py runscript importar_personas --script-args <ruta_archivo_csv>")
        sys.exit(1)
    csv_file_path = args[0]

    oficinas_map = {oficina.nombre_corto: oficina for oficina in Oficina.objects.all()}


    try:
        with open(csv_file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f) 
            personas_a_crear = []
            
            for row in reader:
                nombre= row.get('nombre')
                apellido = row.get('apellido')
                edad = row.get('edad')
                oficina_nombre_corto = row.get('oficina_nombre_corto')

                if not nombre or not apellido or not edad:
                    print(f"Error en la fila {row}. Falta el nombre, apellido o edad.")
                    continue

                try:
                    edad_int = int(edad)
                except (ValueError, TypeError):
                    print(f"Error en la fila {row}. Edad invalida.")
                    continue

                oficina_obj = None
                if oficina_nombre_corto:
                    oficina_obj = oficinas_map.get(oficina_nombre_corto)
                    if not oficina_obj:
                        print(f"Error en la fila {row}. Oficina con nombre corto '{oficina_nombre_corto}' no existe.")
                        print(f"Se creara el registro sin oficina.")
                else:
                    print(f"Advertencia: La persona '{nombre} {apellido}' no tiene oficina asignada. Se creará sin oficina.")

                try:
                    persona = Persona(nombre=nombre, apellido=apellido, edad=edad_int, oficina=oficina_obj)
                    persona.full_clean()
                    personas_a_crear.append(persona)
                except ValidationError as e:
                    print(f"Error de validacion en la fila {row}. Detalles: {e}")
                except Exception as e:
                    print(f"Error inesperado en la fila {row}. Detalles: {e}")

            with transaction.atomic():
                Persona.objects.bulk_create(personas_a_crear)
                print(f"Se importaron {len(personas_a_crear)} registros.")

    except FileNotFoundError:
        print(f"Error; No se encontro el archivo {csv_file_path}")
    except Exception as e:
        print(f"Error inesperado. Detalles: {e}")

