#Inventario es donde se almacenan los datos proporcionados por el usuario   
inventario = []
#Funcion numero 1 destinada para anadir productos
def añadir_producto():
    while True:
        try:
            producto = input("Ingresa el nombre del producto: ")
            precio = float(input("Ingresa el precio del producto: "))
            cantidad = int(input("Ingresa la cantidad del producto: ")) 

            tempInventario = {"producto": producto,
                               "precio": precio, 
                               "cantidad": cantidad,
                               }
            
            inventario.append(tempInventario)

            print(f"{producto} se ingreso con exito")

            break 
        except ValueError:
            print("Ingresa valores validos")
#Funcion numero 2 destinado para mostrar productos
def mostrar_producto():
    if not inventario:
        print("El inventario esta vacio")
    else: 
        for item in inventario:
            print(f"producto: {item['producto']}| cantidad: {item['cantidad']}| precio: {item['precio']} ")
        
#Funcion numero 3 destinada para mostrar un costo total
def costo_total():
    
    for item in inventario:
        subtotal = item['precio'] * item['cantidad']
        print(f"El subtotal a pagar de {item['producto']} es: {subtotal}")

    total = 0
    for i in inventario:
        total += i['precio'] * i['cantidad']
    
    print(f"El total a pagar por los productos es ${total}")