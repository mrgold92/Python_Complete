from Modulos.GestionEscuela import Alumno
import sys

# Importamos el paquete(carpeta) Modulo2 y se aplican los imports definidos en el fichero __init__.py
import ModulosEscuela

alumno = Alumno("Ana", "Sánchez", "Sanz")

print(f"Me llamo: {alumno.Nombre} {alumno.Apellido1} {alumno.Apellido2}")
print(f"Me llamo: {alumno.getNombreCompleto()}")