# Taller numero 1 
""" name = input("Ingrese su nombre: ")
age = int(input("Ingrese su edad: "))

print(f"Hola, {name}. Tienes {age} años. ")
 """
#..........................................................
# Taller, punto numero 2 

""" num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))

result = num1 + num2
print(result) """

#..........................................................
# Taller, punto numero 3

""" print(f"AREA DEL TRIANGULO")
altura = int(input("Ingrese la altura del triangulo: "))
base = int(input("Ingrese la base del triangulo: "))

result = base * altura / 2

print(f"El area del triangulo es: {result}")
 """

#..........................................................
# Taller, punto numero 4

""" print("Conversor de Celsius a Fahrenheit")

celsius = float(input("Ingrese los grados celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"El resultado es: {fahrenheit}")

 """

#..........................................................
# Taller, punto numero 5
""" 
name = input("Ingrese su nombre: ")
age = int(input("Ingrese su edad: "))
height = float(input("Ingrese su altura: "))

print(type(name), type(age), type(height)) """

#..........................................................
# Taller, punto numero 6

""" print(f"CALCULADORA DE EDAD FUTURA: ")
edad_actual = int(input("Ingrese su edad: "))
años = int(input("Ingrese la cantidad de años en el futuro: "))
edad_futura = edad_actual + años
print(f"En {años} años, tendras {edad_futura} años. ") """

#.........................................................
# Taller, punto numero 7
""" 
age = int(input("Ingrese su edad: "))
if age > 18: 
    print("Es mayor de edad")
else: print("Es menor de edad")
 """

#.........................................................
# Taller, punto numero 8

""" num = int(input("Ingrese un numero: "))
if num > 0: 
    print(f"Positivo")
elif  num < 0:
    print(f"Negativo")
else: 
    print(f"0")
 """

#.........................................................
# Taller, punto numero 9
""" print("NUMERO IMPAR O PAR")
num = int(input("Ingrese un numero: "))
if num % 2 == 0:
    print("PAR")
else: 
    print("IMPAR")
    """

#.........................................................
# Taller, punto numero 10

""" num1 = float(input("Ingrese el numero 1: "))
num2 = float(input("Ingrese el numero 2: "))
operation = int(input("Ingrese 1.Suma 2.Multiplicacion 3.Resta 4.Division: "))

if operation == 1:
    result = num1 + num2
    print(result)
elif operation == 2: 
    result = num1 * num2
    print(result)
elif operation == 3:
    result = num1 - num2
    print(result)
else: 
    result = num1/num2
    print(result)
 """

#...........................................................
# Taller, punto numero 11

""" nota = float(input("Ingrese la nota: "))
if nota == 5.0:
    print("EXCELENTE")
elif nota >= 3.0: 
    print("Aprobado")
else: 
    print("Reprobado")
 """

#...........................................................
# Taller, punto numero 12
""" 
num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
num3 = int(input("Ingrese el numero 3: "))
if num1 > num2 and num1 > num3: 
    print("El numero 1 es mayor que el resto")
elif num2 > num1 and num2 > num3:
    print("El numero 2 es mayor que el resto")
else: 
    print("El numero 3 es mayor que el resto")

 """

#...........................................................
# Taller, punto numero 13

""" usernum = int(input("Ingrese un numero hasta donde llegara el contador: "))
for i in range (1,usernum +1):
    print(i)
 """
#...........................................................
# Taller, punto numero 14

""" print("TABLAS DE MULTIPLICAR")
num1 = int(input("Ingresa un numero: "))

for i in range (1,11):
    print(f"{num1} x {i} = {num1 * i}")
 """
#............................................................
# Taller, punto numero 15
""" 
print("CUENTA REGRESIVA")
num = int(input("Ingrese un numero: "))

while num != 0:
    print(num)
    num -=1 """

#.............................................................
# Taller, punto numero 15

""" import random  
num = int(input("Ingrese un numero: "))
machine = random.choice(range(1,11))
print (machine)

if num == machine:
    print(f"La eleccion es la misma")
else:  
    print(f"La eleccion es diferente")
 """

#................................................................
# Taller, punto numero 18

""" num = int(input("ingrese un numero: "))
suma = 0
while num != 0:
    suma +=num
    num = int(input("ingrese un numero: "))
print(f"el total es {suma}") """

#................................................................
# Taller, punto numero 19
""" 
list = ["manzana, pera, guayaba, ochuva"]
print(*list)
 """

#..................................................................
# Taller, punto numero 20 y 21

""" frutas = []
lista = input("Ingresa lo que quieras a la lista: ")
frutas.append(lista)
print(*frutas)
option = input("Desea eliminar un producto? (si/no): ")
if option == "si":
    deletee = input("Eliminar producto: ")
    frutas.remove(deletee)
    print(*frutas) 
elif option == "no":
    print("Gracias")

print("Verificacion de producto en la lista")
lista = input("Ingrese el producto a buscar: ")
if lista in frutas:
    print("El producto si esta en la lista")
else: 
    print("El producto no esta en la lista")
    

 """
#..................................................................
# Taller, punto numero 22
""" 
numbers = []
amount = int(input("Cuantos numeros desea ingresar?: "))
for i in range(amount):
    num = int(input("Ingrese un numero: "))
    numbers.append(num) 
promedio = sum(numbers) / len(numbers)
print("Numeros ingresados:", numbers)
print("Promedio:", promedio)  """

#...................................................................
# Taller, punto numero 23 

""" pares = []

amount = int(input("Ingrese la cantidad de numeros que quiere ingresar: "))

for i in range(amount): 
    num = int(input(f"Ingresa el numero: "))
    if num % 2 == 0: 
        pares.append(num)
print("La lista de pares:", pares) """

#...................................................................
# Taller, punto numero 24 

""" lista = [100,100,102,102,103,103,104]
not_duplicated = list(set(lista))

print(not_duplicated) """
