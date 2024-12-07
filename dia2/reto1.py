for num in range(100):
        #ENTRADA
        OPERACION = int(input(""" Ingrese la operacion a realizar
                            1) Soles a Dolares
                            2) Dolares a Soles
                            ESCOGA LA OPCIÓN: """))
        
        cantidad = int(input("¿Cuánto desea cambiar? "))
        
        cambio = float(input("Ingrese el tipo de cambio: "))
        
        #Operacion
        
        if OPERACION == 1:
            print(f"La conversion de soles a dolares es {cantidad/cambio}")
            
        elif OPERACION == 2:
            print(f"La conversion de dolares a soles es {cantidad*cambio}")
            
        #SALIDA
        consulta = input ("¿Desea continuar con la operación? (si/no): ")
        if consulta == "no":
            print("Gracias")
            break