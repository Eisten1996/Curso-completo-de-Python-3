# 1. Crear una variable 'inicio' con el valor 1
# 2. Crear una variable 'fin' con el valor 6
# 3. Hacer un bucle while que muestre tantas filas como valores haya entre 'inicio' y 'fin'
# 4. En cada interaccion del bucle mostrar el texto 'Esta es la fila' + numero de fila en la que esta

inicio = 1
fin = 6

while (inicio < fin):
    # print('Esta es la fila {}'.format(inicio))
    print('Esta es la fila '+str(inicio))
    inicio = inicio + 1
