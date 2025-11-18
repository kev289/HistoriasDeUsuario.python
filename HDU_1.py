# Intenta toda la linea de codigo para que si algun dato no esta en el parametro lance el except e imprima dato incorrecto
try:
    #Declaro las variables y le solicito al usuario los datos de el producto 
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    costo_total = precio * cantidad  

    print(f"Nombre:", nombre, "Precio:", precio, "Cantidad:", cantidad, "Costo total: ", costo_total  )
    
except  ValueError: 
    print("Dato Incorrecto") 

#Es un inventario donde imprime el nombre, precio, cantidad y costo total.
