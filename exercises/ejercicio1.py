while True: 
    try:
        farenheit = 9/5 + 32
        celsius = float(input("Ingrese los grados celsius que desea convertir a farenheit: "))
        resultado = celsius * farenheit
        print(resultado)
        option = int(input("¿Deseas continuar? (1.No/2.Si)"))
        if option == 1:
            print ("Adios!")
            break
        else:
            continue
    except: 
        print("Ingrese un numero valido")
