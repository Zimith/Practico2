import csv
import sys
from django.db import transaction
from django.core.exceptions import ValidationError
from oficina.models import Oficina

def run(*args):
    if not args:
        print("Error: Favor proporcionar la ruta de archivo")
        print("Uso: ./manage.py  runscript importar_oficinas --script-args <ruta_archivo_csv>")
        sys.exit(1)

    csv_file_path = args[0]
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            oficinas_a_crear = []

            for row in reader:
                nombre = row.get('nombre')
                nombre_corto = row.get('nombre_corto')

                if not nombre or not nombre_corto:
                    print("Error en la fila {row}. Falta un campo")
                    continue

                try:
                    oficina = Oficina(nombre=nombre, nombre_corto=nombre_corto)
                    oficina.full_clean()
                    oficinas_a_crear.append(oficina)
                except ValidationError as e:
                    print(f"Error de validacion en la fila {row}. Detalles: {e}")

                except Exception as e:
                    print(f"Error inesperado en la fila {row}. Detalles: {e}")


            with transaction.atomic():
                Oficina.objects.bulk_create(oficinas_a_crear)
                print(f"Importacion  de {len(oficinas_a_crear)} oficinas completada.")

    except FileNotFoundError:
        print(f"Error; No se encontro el archivo {csv_file_path}")
    except Exception as e:
        print(f"Error inesperado. Detalles: {e}")
