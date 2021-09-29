frase = input("Escribe una frase: ")
letra = ""

while (len(letra) != 1):                # mientras número de caracteres de letra sea distinto de 1
    letra = input("Escribe una letra: ")
    if (len(letra) != 1):
        print(f"{letra}, no es valido")
    elif (letra.isdigit() == True):
        print(f"{letra}, no es valido")
        letra = ""

###############################################################

index = 0  # variable que funciona como indice de la colección
contador = 0  # varibale que utilizamos para contar las coincidencias
while (index < len(frase)):  # mientras valor de INDEX sea inferior al número de elementos de la colección (número de caracteres de la frase)
    if(frase[index].lower() == letra.lower()):
        contador += 1
    index += 1

###############################################################

print(f"La letra {letra} aparece en la frase {contador} veces")
