#----------------------------------------------------------------#
# Los conjuntos son una colección de elementos sin índice,
# se dice que está desordenado.
#
# En un conjunto se pueden añadir y eliminar elementos.
#
# Para acceder a los valores tenemos que recorrer la colección
# con for.
#-----------------------------------------------------------------#

# Declaración del conjunto
set1 = {"java", "pyhton", "android", "php"}

# Añadir un elemento al conjunto
set1.add("javascript")

# Eliminar un elemento del conjunto
set1.discard("android")

# Imprime la longitud del conjunto
print(len(set1))

# Imprime el conjunto {...,...}
print(set1)

# Recorre el conjunto y muestra el valor
for s in set1:
    print(s)
