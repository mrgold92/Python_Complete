#####################################################################
# Declaración de Variables                                          #
#####################################################################
#                                                                   #
#   Sintaxis: [nombre de la varible] = [valor inicial]              #
#                                                                   #
#   Ejemplos:                                                       #
#       numero = 20                                                 #
#       saludo = "Hola a todos !!!"                                 #
#                                                                   #
#####################################################################

# Declaramos tres variables y asignamos un valor inicial
numero = 10
Numero = 20
saludo = "Hola mundo !!!"

# Mostramos el contenido de las variables por pantalla
print(numero)
print(Numero)
print("Saludo: " + saludo)
print("")

# Mostramos el tipo de las variables por pantalla
print(type(numero))
print(type(saludo))
print("")

# Consultamos el tipo de diferentes valores utilizando la función TYPE
print(type(3))  # int
print(type(3.1))  # float
print(type("3"))  # str
print(type("pizza"))  # str
print(type(1 == 1))  # bool
print(type(('1', '2', '3')))  # tuple
print(type(['1', '2', '3']))  # list
print(type({"1", "2", "3"}))  # set
