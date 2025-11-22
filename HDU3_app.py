from defs_HDU3 import inicializar, save, addProduct, show, search, update, deletee, stadistic

while True:
    print("--- MENÚ PRINCIPAL ---")
    print("1. AGREGAR PRODUCTO")
    print("2. MOSTRAR PRODUCTO")
    print("3. BUSCAR PRODUCTO")
    print("4. ACTUALIZAR PRODUCTO")
    print("5. ELIMINAR PRODUCTO")
    print("6. ESTADISTICAS")
    print("7. GUARDAR CSV")
    print("8. CARGAR CSV")
    print("9. SALIR")

    while True:
        try:
            opt = int(input("SELECCIONA UNA OPCION DE 1 A 9: "))
            break
        except ValueError:
            print("ERROR EL VALOR DEBE SER NUMERICO")

    if opt == 1:
        global countPrice, countQuantity
        countPrice = 0
        countQuantity = 0
        id = int(input("INGRESE EL ID DEL PRODUCTO: "))
        name = input("INGRESE EL NOMBRE: ")
        price = int(input("INGRESE EL PRECIO: "))
        countPrice += price
        quantity = int(input("INGRESE LA CANTIDAD: "))
        countQuantity += quantity
        addProduct(id, name, price, quantity)

    elif opt == 2:
        show()

    elif opt == 3:
        name = input("INGRESE EL NOMBRE DEL PRODUCTO QUE DESEAS BUSCAR: ")
        search(name)

    elif opt == 4:
        id = int(input("INGRESA EL ID: "))
        name = input("INGRESA EL NOMBRE: ")
        price = int(input("INGRESE UN PRECIO: "))
        quantity = int(input("INGRESE UNA CANTIDAD: "))
        update(id, name, price, quantity)

    elif opt == 5:
        name = input("INGRESE EL NOMBRE: ")
        deletee(name)

    elif opt == 6:
        stadistic()
        
    elif opt == 7:
        print("")
    elif opt == 8:
        print("")
    elif opt == 9:
        print("HASTA LUEGO MUCHAS GRACIAS.")
        break
    