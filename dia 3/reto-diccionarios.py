import os
from time import sleep

"""
CRUD
-CREATE
-READ
-UPDATE
-DELETE
"""

dic_empresas = {
    '12345678901': {
        'razon_social': 'EMPRESA 1',
        'direccion': 'Calle los girasoles 123'
    }
}

ANCHO = 50
opcion = 0

while opcion < 5:
    os.system("clear")
    print("=" * ANCHO)
    print(" " * 10 + "GESTION DE EMPRESAS")
    print("=" * ANCHO)
    print("""
          [1] REGISTRAR EMPRESA
          [2] MOSTRAR EMPRESA
          [3] ACTUALIZAR EMPRESA
          [4] ELIMINAR EMPRESA
          [5] SALIR
          """)
    print("-" * ANCHO)
    opcion = int(input("INGRESE OPCION: "))
    os.system("clear")

    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "[1] REGISTRAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("RUC          : ")
        razon_social = input("RAZON SOCIAL : ")
        direccion = input("DIRECCION    : ")
        dic_nueva_empresa = {
            ruc: {
                'razon_social': razon_social,
                'direccion': direccion,
            }
        }
        dic_empresas.update(dic_nueva_empresa)
    elif opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "[2] MOSTRAR EMPRESAS")
        print("=" * ANCHO)
        for ruc, datos in dic_empresas.items():
            print(f"RUC          : {ruc}")
            print(f"Razon Social : {datos['razon_social']}")
            print(f"Direccion    : {datos['direccion']}")
            print("*" * ANCHO)
        input("Presione ENTER para continuar...")
    elif opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "[3] ACTUALIZAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("INGRESE RUC DE LA EMPRESA A ACTUALIZAR: ")
        if ruc in dic_empresas:
            print(f"EMPRESA A ACTUALIZAR: {dic_empresas[ruc]['razon_social']}")
            nueva_razon_social = input('RAZON SOCIAL : ')
            nueva_direccion = input('DIRECCION    : ')
            dic_nueva_empresa = {
                ruc: {
                    'razon_social': nueva_razon_social,
                    'direccion': nueva_direccion,
                }
            }
            dic_empresas.update(dic_nueva_empresa)
            print("EMPRESA ACTUALIZADA CON EXITO")
        else:
            print("NO SE ENCONTRO LA EMPRESA")
    elif opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "[4] ELIMINAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("INGRESE EL RUC DE LA EMPRESA A ELIMINAR: ")
        if ruc in dic_empresas:
            dic_empresas.pop(ruc)
            print("EMPRESA ELIMINADA")
        else:
            print("NO SE ENCONTRO LA EMPRESA")
    elif opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "[5] SALIR")
        print("=" * ANCHO)
    else:
        print("=" * ANCHO)
        print(" " * 10 + "OPCION INVALIDA!!!")
        print("=" * ANCHO)
    sleep(1)
