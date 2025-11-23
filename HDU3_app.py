#De mi carpeta de funciones importo todas las funciones creadas
from defs_HDU3 import inicializar, save, addProduct, show, search, update, deletee, stadistic,saveCsv, loadCsv

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
#bucle while para repetir la opcion de seleccionar un numero de el menu
    while True:
        try:
            opt = int(input("SELECCIONA UNA OPCION DE 1 A 9: "))
            break
        except ValueError:
            print("ERROR EL VALOR DEBE SER NUMERICO")

    if opt == 1:
        #contador global para guardar los datos de precio y cantidad ingresados por el usuario
        global countPrice, countQuantity
        countPrice = 0
        countQuantity = 0   
        #while y todas sus validaciones para que el usuario tenga que ingresar un string
        while True: 
            try: 
                id = int(input("INGRESE EL ID DEL PRODUCTO: "))
                break
            except: ValueError
            print("ERROR EL DATO DEBE SER NUMERICO")
            
        name = input("INGRESE EL NOMBRE: ")
        while True:
            try:  
                price = int(input("INGRESE EL PRECIO: "))
                break
            except: ValueError
            print("ERROR EL DATO DEBE SER NUMERICO")        
            
        countPrice += price
        while True:
            try:
                quantity = int(input("INGRESE LA CANTIDAD: "))
                break
            except: ValueError
            print("ERROR EL DATO DEBE SER NUMERICO")
        countQuantity += quantity
        addProduct(id, name, price, quantity)

    elif opt == 2:
        show()

    elif opt == 3:
        name = input("INGRESE EL NOMBRE DEL PRODUCTO QUE DESEAS BUSCAR: ")
        search(name)

    elif opt == 4:
#bucles while para hacer validaciones y colocar un dato correcto 
        while True:
            try:
                id = int(input("INGRESA EL ID: "))
                break
            except: ValueError
            print("EL DATO DEBE SER NUMERICO")
        name = input("INGRESA EL NOMBRE: ")
        while True:
            try:
                price = int(input("INGRESE UN PRECIO: "))
                break
            except: ValueError
        while True:
            try:
                quantity = int(input("INGRESE UNA CANTIDAD: "))
                break
            except: ValueError
        update(id, name, price, quantity)

    elif opt == 5:
        name = input("INGRESE EL NOMBRE: ")
        deletee(name)

    elif opt == 6:
        stadistic()

    elif opt == 7:
        ruta = "inventario.csv"
        saveCsv(ruta)

    elif opt == 8:
        ruta = "inventario.csv"
        loadCsv(ruta)
#opcion salir con un break para terminar el while true de el menu
    elif opt == 9:
        print("HASTA LUEGO MUCHAS GRACIAS.")
        break
    