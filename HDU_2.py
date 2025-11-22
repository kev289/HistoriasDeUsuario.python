
from defs_hdu2 import añadir_producto, mostrar_producto, costo_total    
#Bucle para seguir ejecutando el codigo hasta que el usuario seleccione la opcion 4 y salir de el menu
while True:
    print("1. Agregar un producto. 2. Mostrar un producto: 3. Costo total. 4. Salir. ")
    option = input("Ingresa una opcion: ")

    if option == "1":
        añadir_producto()
    elif option == "2": 
        mostrar_producto()
    elif option == "3": 
        costo_total()
    elif option == "4": 
        print("Hasta luego")
        break
#else para que si el usuario ingresa un dato invalida me imprima que lo ingrese bien
    else: 
        print("Error ingrese una opcion valida")
                