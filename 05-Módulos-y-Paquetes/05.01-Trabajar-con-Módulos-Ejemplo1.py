
import sys
sys.path.insert(0, '../05-Módulos-y-Paquetes/ModulosEscuela')
import ModulosEscuela.Escuela

# Importamos todo el contenido de un módulo
# Tenemos que utilizar el nombre del Módulo para acceder a sus objetos o funciones

alumno = ModulosEscuela.Escuela.Alumno("Ana", "Sánchez", "Sanz")

print(f"Me llamo: {alumno.Nombre} {alumno.Apellido1} {alumno.Apellido2}")
print(f"Me llamo: {alumno.getNombreCompleto()}")
