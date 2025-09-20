...
## Ejercicio: crear un programa en Python que pida dos números y obtenga como resultado cuál de ellos es par o si ambos lo son
...

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos números son pares.")
elif num1 % 2 == 0:
    print(f"El número {num1} es par.")
elif num2 % 2 == 0:
    print(f"El número {num2} es par.")
else:
    print("Ninguno de los números es par.")