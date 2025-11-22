import csv 
import json
file = "inventory.json"

total = 0

def inicializar():
    try: 
        with open (file, "r") as f: 
            return json.load(f)
    except FileNotFoundError:
        return{}

def save(data): 
    with open(file, "w") as f:
        json.dump(data,f, indent = 4 )

def addProduct(id, name,price,quantity):
    data = inicializar()
    data[id] = {'name' : name, 'price' : price, 'quantity' : quantity}
    save(data)
    print("PRODUCTO CREADO.")

def show(): 
    data = inicializar()
    if not data:
        print("NO HAY NADA DENTRO")

    for name, info in data.items():
        print(name, info )

def search(name):
    data = inicializar()
    for key,info in data.items(): 
        if info['name'] == name:
            print("ENCONTRADO", info)
            return
    else:
        print("NO ENCONTRADO")

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

        
       
       

def stadistic():
    data = inicializar()
    total = 0
    for name, info in data.items():
        print(f"{name}, {info} \n")
        totalCost = info['price'] * info['quantity']
        total = totalCost
        save(data)
    
    print(f"EL PRECIO TOTAL DEL CARRITO ES: {total}")
