frutas1 = ["manzana", "pera"]
frutas2 = ["manzana", "pera"]
frutas3 = frutas1

print(frutas3 is frutas1)

frutas3.append("fresa")

print(frutas1)

print(frutas3 is frutas1)
print(frutas3 is not frutas1)
