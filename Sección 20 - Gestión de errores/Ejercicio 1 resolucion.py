# Crear la funcion "operacion" que dados 3 numeros, divida el primer numero entra la resta de los otros dos numeros

# Utilizar la funcion creada con los numeros 5, 4, 2
# Utilizar la funcion creada con los numeros 6, 3, 3

# Utilizar el bloque try ... except para controlar cualquier posible error

def operacion(numero1, numero2, numero3):
    resultado = numero1 / (numero2-numero3)
    return resultado


try:
    resultado = operacion(5, 4, 2)
    print(resultado)
    resultado = operacion(6, 3, 3)
    print(resultado)
except:
    print("Hay un error")
