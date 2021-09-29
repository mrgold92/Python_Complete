from datetime import datetime

fecha = input("Escribe tu fecha de nacimiento: ")
fnDt = datetime.strptime(fecha, "%d-%m-%Y").date()
hoyDt = datetime.now().date()
edad = hoyDt.year - fnDt.year


if(edad >= 18):
    print(f"Tienes {edad} años, eres mayor de edad.")
else:
    años = 18 - edad
    print(f"Te faltan {años} años para ser mayor de edad.")
