# Condicionales (if, elif, else)

a = 8
b = 4

print(a > b)

print(a < b)

if (a > b):
    print("a es mayor que b")

if (a < b):
    print("a es mayor que b")

c = 2
d = 6

if (a > c) and (b < d):
    print("la primera expresion es correcta")

if (a > c) and (b > d):
    print("la primera expresion es correcta")

if (a > c) and (b > d):
    print("la primera expresion es correcta")
else:
    print("la primera expresion no es correcta")


if (a > b):
    print("a es mayor que b")
elif (a == b):
    print("a es igual a b")
else:
    print("ninguna expresion es correcta")

b = 8

if (a > b):
    print("a es mayor que b")
elif (a == b):
    print("a es igual a b")
else:
    print("ninguna expresion es correcta")

b = 10

if (a > b):
    print("a es mayor que b")
elif (a == b):
    print("a es igual a b")
else:
    print("ninguna expresion es correcta")
