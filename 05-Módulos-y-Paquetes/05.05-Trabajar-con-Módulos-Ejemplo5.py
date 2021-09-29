from Modulos.GestionEscuela import Alumno
import sys

import ModulosEscuela

alumno = Alumno("Ana","Sánchez", "Sanz")

print(f"Me llamo : {alumno.Nombre} {Alumno.Apellido1} {alumno.Apellido2}")
print(f"Me llamo: {alumno.getNombreCompleto()}")