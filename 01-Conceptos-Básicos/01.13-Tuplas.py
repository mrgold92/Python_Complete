#----------------------------------------------------------------#
# Las tuplas son una colección de datos ordenados con un
# índice de base 0.
#
# A diferencia de las listas, las tuplas no se pueden modificar.
# Por ejemplo, podríamos utilizar tuplas para:
#
# - Códigos postales.
# - Ciudades.
# - Días de la semana.
# - Etc.
#----------------------------------------------------------------#

numeros = (17, 89, 21, 988, 43, 429, 32, 834)
print(numeros)                    # Imprime la tupla
print(numeros[4])                 # Imprime el valor en la posición 4
print(list(enumerate(numeros)))   # Imprime el valor y su índice
print(max(numeros))               # Valor máximo
print(min(numeros))               # Valor mínimo
print(sum(numeros))               # Suma los valores
