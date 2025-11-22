#Coloco un while true para que me ejecute el codigo hasta que el usuario coloque los datos correctos
while True:
    #Hago un try para que ejecute el codigo desde que los datos proporcionados por el usuario esten correctos 
    try:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        costo_total = precio * cantidad  

        print(f"Nombre:", nombre, "Precio:", precio, "Cantidad:", cantidad, "Costo total: ", costo_total  )
        break
        #El except es para dicho caso en el que el usuario proporcione un dato incorrecto, me imprime datos incorrectos.
    except  ValueError: 
        print("Dato Incorrecto ingrese un valor valido") 
    finally: 
        print("Finalizo el programa")


