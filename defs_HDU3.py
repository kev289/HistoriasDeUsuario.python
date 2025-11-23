#importo csv y json para trabajar con ese formato
import csv 
import json
#este es el inventario json que almacena los productos creados
file = "inventory.json"

total = 0
#funcion inicializar para abrir el archivo json 
def inicializar():
    try: 
        with open (file, "r") as f: 
            return json.load(f)
    except FileNotFoundError:
        return{}
#funcion save para guardar los datos en archivo json
def save(data): 
    with open(file, "w") as f:
        json.dump(data,f, indent = 4 )
#funcion principal para guardar id nombre precio y cantidad en el archivo json
def addProduct(id, name,price,quantity):
    data = inicializar()
    data[id] = {'name' : name, 'price' : price, 'quantity' : quantity}
    save(data)
    print("PRODUCTO CREADO.")
#funcion para mostrar lo que hay dentro del inventory.json 
def show(): 
    data = inicializar()
    if not data:
        print("NO HAY NADA DENTRO")

    for name, info in data.items():
        print(name, info )
#funcion para buscar el nombre e imprimir la informacion que hay dentro del archivo 
def search(name):
    data = inicializar()
    for key,info in data.items(): 
        if info['name'] == name:
            print("ENCONTRADO", info)
            return
    else:
        print("NO ENCONTRADO")
#funcion para actualizar ya sea nombre precio o cantidad
def update(id, name = None, price = None, quantity = None):
    data = inicializar()
    id = str(id)
    if id in data:
        if name:
            data[id]["name"] = name
        if price:
            data[id]["price"] = price
        if quantity:
            data[id]["quantity"] = quantity
        save(data)
        print("Producto actualizado.")
    else:
        print("Producto no encontrado.")
#funcion para eliminar datos dentro del archivo json
def deletee(name):
    data = inicializar()
    keyDelete = None
    for key, info in data.items():
        if info['name'] == name:
            keyDelete = key
            break  

    
    if keyDelete is None:
        print("NO ENCONTRADO")
        return

    
    del data[keyDelete]
    save(data) 
    print("PRODUCTO ELIMINADO")
#funcion para imprimir el costo total del producto almacenado
def stadistic():
    data = inicializar()
    total = 0
    for name, info in data.items():
        print(f"{name}, {info} \n")
        totalCost = info['price'] * info['quantity']
        total = totalCost
        save(data)
    
    print(f"EL PRECIO TOTAL DEL CARRITO ES: {total}")

def saveCsv(ruta):
    data = inicializar()

    
    if not data: 
        print("EL INVENTARIO NO CONTIENE NINGUNA INFORMACION.")
        return
    
    try: 
        with open (ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(["nombre","precio","cantidad"])

            for key, info in data.items():
                writer.writerow([info["name"], info["price"], info["quantity"]])

        print(f"Inventario guardado correctamente.{ruta}")

    except PermissionError:
        print("No tienes permisos para guardar en este ruta.")
    except Exception as e:
        print(f"Error inesperado. {e}")

def loadCsv(ruta):
    data = inicializar()
    loadedProducts = {}
    invalidRows = 0

    try: 
        with open(ruta, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            filas = list(reader)
    except FileNotFoundError:
        print("Error: el archivo no fue encontrado.")
        return
    except UnicodeDecodeError:
        print("El archivo con codificación inválida.")
        return
    
    if not filas: 
        print("Error: El archivo está vacío.")
        return 
    
    header = [c.strip().lower() for c in filas[0]]
    if header != ["nombre","precio","cantidad"]:
        print("Error: El encabezado del CSV no es válido.")
        return
    
    for row in filas[1:]:
        if len(row) != 3:
            invalidRows +=1
            continue

        nombre, precio, cantidad = row

        try:
            precio = float(precio)
            cantidad = int(cantidad)
            if precio < 0 or cantidad < 0:
                raise ValueError
        except ValueError:
            invalidRows +=1 
            continue

        loadedProducts[nombre] = {
            "name": nombre,
            "price": precio,
            "quantity": cantidad
        }

    if not loadedProducts:
        print("Error: no se cargó ningún producto.")
        if invalidRows:
            print(f"{invalidRows} filas inválidas fueron omitidas.")
        return
    
    option = input("¿Deseas sobrescribir el inventario actual? (SI/NO) ").strip().upper()
    
    if option == "SI":
        # IDs consecutivos desde 1
        data.clear()
        for i, (nombre, info) in enumerate(loadedProducts.items(), start=1):
            data[str(i)] = info
        action = "Inventario reemplazado."
    else:
        # Fusionar: IDs continuos después del mayor existente
        next_id = max([int(k) for k in data.keys()], default=0) + 1
        for nombre, info in loadedProducts.items():
            id_exist = None
            for id_prod, prod_info in data.items():
                if prod_info["name"].lower() == nombre.lower():
                    id_exist = id_prod
                    break
            if id_exist:
                data[id_exist]["quantity"] += info["quantity"]
                data[id_exist]["price"] = info["price"]
            else:
                data[str(next_id)] = info
                next_id += 1
        action = "Inventario fusionado."

    save(data)

    print("\n--- RESULTADO DE LA CARGA DE CSV ---")
    print(f"Productos cargados válidos: {len(loadedProducts)}")
    print(f"Filas inválidas omitidas: {invalidRows}")
    print(action)

    return data