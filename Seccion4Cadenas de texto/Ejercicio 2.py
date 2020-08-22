# Crea una variable "cadena" que contiene el texto "Esto es un texto de ejemplo"
# Crea una variable "longitud" que contiene la longitud(numero de caracteres) de la variable "cadena"
# Crea una variable "mayusculas" que contiene la variable "cadena" en mayusculas
# Crea una variable "resultado" que contiene la variable "mayusculas" y la variable "resultado" convertida a string

cadena = "Esto es un texto de ejemplo"
print(cadena)
longitud = len(cadena)
print(longitud)
mayusculas = cadena.upper()
print(mayusculas)
resultado = mayusculas+" tiene longitud de: "+str(longitud)
print(resultado)
