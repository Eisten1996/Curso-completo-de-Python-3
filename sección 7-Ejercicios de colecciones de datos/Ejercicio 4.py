# 1. Crear un "diccionario" con los pares valores siguientes
#       clave = uno valor = one
#       clave = dos valor = two
#       clave = tres valor = three
# 2. Mostrar por pantalla el valor de la variable "diccionario"
# 3. Añadir un nuevo elemento al diccionario
#       clave = cuatro valor = four
# 4. Mostrar ahora el valor de la variable "diccionario"
# 5. Recoger un valor introducido por teclado y almacenarlo en "dato"
# 6. Utilizar "dato" como clave del diccionario para recuperar su valor

diccionario = {
    'uno': 'one',
    'dos': 'two',
    'tres': 'three'
}

print(diccionario)

diccionario['cuatro'] = 'four'

print(diccionario)

dato = input()

print(diccionario[dato])
