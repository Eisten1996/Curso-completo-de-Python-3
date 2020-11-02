# for
colores = ['rojo', 'azul', 'verde']

for color in colores:
    print(color)
print('---------------------------------------------------------------------')

cadena = 'Hola mundo'

for caracter in cadena:
    print(caracter)
print('---------------------------------------------------------------------')

for numero in range(8):
    print(numero)
print('---------------------------------------------------------------------')

for numero in range(3, 8):
    print(numero)
print('---------------------------------------------------------------------')

for numero in range(3, 8, 2):
    print(numero)
print('---------------------------------------------------------------------')

# break - para parar el bucle
for numero in range(10):
    if (numero == 5):
        break
    print(numero)
print('---------------------------------------------------------------------')

# continue - para parar solo la iteracion actual
for numero in range(10):
    if (numero == 6):
        continue
    print(numero)
print('---------------------------------------------------------------------')

# for doble
for numero1 in range(4):
    for numero2 in range(3):
        print(numero1, numero2)
