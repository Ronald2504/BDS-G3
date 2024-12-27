import os
from time import sleep
from matriculas.lib_alumnos import *  ##IMPORTO LA CARPETA Y ARCHIVO, IMPORT ES IMPORTAR LAS FUNCIONES DEL ARCHIVO

"""
CRUD
 - CREATE
 - READ
 - UPDATE
 - DELETE
"""
cargar_alumnos('alumnos.txt') #FUNCION DENTRO DE LIB ALUMNOS, PARAMETRO TIENE EL NOMBRE DEL ARCHIVO DONDE TIENEN LOS DATOS, ALUMNOS
opcion = 0 #YA QUE ES UN CICLO WHILE COMIENZA CON 0 PERO EN CASO CAMBIE ESTE EJECUTA UNA FUNCION

while(opcion < 5): #SI LA OPCION ES MENOR A 5 EJECUTA LO SIGUIENTE
    os.system("clear") #LIMPIA LA PANTALLA
    menu()             #LLAMA LA FUNCION MENU 
    opcion = int(input("INGRESE OPCION : "))  #INGRESAR LA OPCION Y CONVIERTE EN ENTERO
    os.system("clear") #LIMPIA LA PANTALLA
    if opcion == 1:
        registrar() #MANDA LA FUNCION REGISTRAR
    elif opcion == 2:
        mostrar()
        input("Presion ENTER para continuar...")
    elif opcion == 3:
        actualizar()
    elif opcion == 4:
        eliminar()
    elif opcion == 5:
        grabar_alumnos('alumnos.txt')
        mostrar_mensaje("[5] SALIR")
    else:
        mostrar_mensaje("OPCIÓN INVÁLIDA!!!")
    sleep(1)