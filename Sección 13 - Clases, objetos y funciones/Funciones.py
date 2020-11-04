# Funciones
# def saludar():
#     print('Buenos dias')


# saludar()


def saludar(nombre):
    print('Buenos dias {}'.format(nombre))


nombre = 'Dipper'

saludar(nombre)


def sumar(numero1, numero2):
    suma = numero1+numero2
    return suma


numero1 = 5
numero2 = 3

print(sumar(numero1, numero2))


# paso de valor por referencia
colores = ['rojo', 'verde', 'azul']


def incluir_color(colores, color):
    colores.append(color)


color = 'negro'

incluir_color(colores, color)

print(colores)
