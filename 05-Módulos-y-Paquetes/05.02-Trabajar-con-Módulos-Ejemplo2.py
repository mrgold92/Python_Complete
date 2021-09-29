from ModulosEscuela.Escuela import Alumno
import sys
sys.path.insert(0, '/05-Módulos-y-Paquetes/ModulosEscuela')

# Importamos un objeto o función de un módulo
# Si queremos importar varios lo separamos por comas

alumno = Alumno("Ana", "Sánchez", "Sanz")

print(f"Me llamo: {alumno.Nombre} {alumno.Apellido1} {alumno.Apellido2}")
print(f"Me llamo: {alumno.getNombreCompleto()}")
