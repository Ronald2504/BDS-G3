import os 
from time import sleep

#PROGRAMA PARA CONVERTIR DE SOLES A DOLARES Y DOLARES A SOLES
#ENTRADA

TIPO_DE_COMPRA = 3.7
TIPO_DE_VENTA = 3.8
bandera = True
#PROCESO

while(bandera):
    print("""
          ======================================
               CONVERTIDOR DE MONEDAS
          ======================================
            [1] CONVERTIDOR SOLES A DOLARES
            [2] CONVERTIDOR DOLARES A SOLES
            [3] SALIR
          ======================================
            """)
    opcion = int(input("ELIJA UNA OPCION: "))
    os.system("clear")
    if(opcion == 1):
        print("""
              ======================================
                    CONVERTIR SOLES A DOLARES
              ======================================
              """)
        monto_origen = float(input("INGRESE MONTO EN SOLES: "))
        monto_destino = monto_origen / TIPO_DE_VENTA
        print(f"EL MONTO EN DOLARES ES {monto_destino}")
    elif(opcion == 2):
        print("""
              ======================================
                    CONVERTIR DOLARES A SOLES
              ======================================
              """)
        monto_origen = float(input("INGRESE MONTO EN DOLARES: "))
        monto_destino = monto_origen * TIPO_DE_COMPRA
        print(f"EL MONTO EN SOLES ES {monto_destino}")
    elif(opcion == 3):
        bandera = False
        print("SALIENDO DEL PROGRAMA...")
    else:
        print("OPCION NO VALIDA!!")
        break
    sleep(4)
    os.system("clear")

# SALIDA