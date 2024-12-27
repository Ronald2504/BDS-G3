ANCHO = 20

dic_alumnos = {}                #DICCIONARIO VACIO

def cargar_alumnos(file_name):                  #RECIBIR EL ARCHIVO
    file = open(file_name,'r')                  #LO ABRE EN MODO LECTURA
    str_alumnos = file.read()                   #LEE CONTENIDO DEL ARCHIVO Y GUARDA EN STR_ALUMNOS
    file.close()                                #CIERRA ARCHIVO
    lista_alumnos = str_alumnos.splitlines()    #EL CONTENIDO LO SEPARA POR CADA ENTER(SALTO DE LINEA)
    for str_fila in lista_alumnos:              #SEPARA LOS ELEMENTOS POR COMAS
        lista_fila = str_fila.split(',')        #SEPARA LOS ELEMENTOS POR COMAS
        dic_fila = {
            'nombre':lista_fila[1],             #CREA EL DICCIONARIO, CLAVE NOMBRE Y ASIGNA VALOR
            'email':lista_fila[2]               #CREA EL DICCIONARIO, CLAVE NOMBRE Y ASIGNA VALOR
        }
        dic_nuevo_alumno = {                    #CREA UN NUEVO DICCIONARIO DONDE LA CLAVE ES LISTA FILA 0 CON LOS DATOS DEL DIC_FILA ANTERIOR
            lista_fila[0]: dic_fila             #CREA UN NUEVO DICCIONARIO DONDE LA CLAVE ES LISTA FILA 0 CON LOS DATOS DEL DIC_FILA ANTERIOR
        }
        dic_alumnos.update(dic_nuevo_alumno)    #ACTUALIZA EL DICCIONARIO VACIO CON LOS DATOS DE DIC NUEVO ALUMNO

def grabar_alumnos(file_name):                  #UTILIZA LA FUNCION GRABAR EN EL TEXTO LLAMADO FILE_NAME
    str_alumnos = ""                            #EL TEXTO COMIENZA EN BLANCO
    for alumno_clave,alumno_valor in dic_alumnos.items():    #REGISTRA EL DNI DEL ALUMNO EN STR 
        str_alumnos += alumno_clave           #REGISTRA EL DNI DEL ALUMNO EN STR 
        for registro_clave,registro_valor in alumno_valor.items():   #BUSCA LOS VALORES EN ALUMNO VALOR 
            str_alumnos += registro_valor         #REGISTRA LOS VALORES EN STR
            if registro_clave != 'email':           #SI LA CLAVE NO ES EMAIL SE AGREGA UNA COMA
                str_alumnos += ','
            else:
                str_alumnos += '\n'              #SI EL VALOR ES EMAIL SE DA UN ESPACIO
    
    fsalida = open(file_name,'w')         #ABRE EL ARCHIVO FILE NAME
    fsalida.write(str_alumnos)            #ESCRIBRE LOS DATOS DEL ARCHIVO
    fsalida.close()                       #SE CIERRA EL ARCHIVO
    



def mostrar_mensaje(texto):
    print("*" * ANCHO + "*" * ANCHO)
    if texto != " ":
        print(" " * 10 + texto)
        print("*" * ANCHO + "*" * ANCHO)

def menu():                                  #FUNCION MENU
    mostrar_mensaje("GESTIÓN DE ALUMNOS")    #MUESTRA EL MENSAJE Y LLAMA A LA FUNCION MOSTRAR MENSAJE
    print("""                                
         [1] REGISTRAR ALUMNO
         [2] MOSTRAR ALUMNOS
         [3] ACTUALIZAR ALUMNO
         [4] ELIMINAR ALUMNO
         [5] SALIR
          """)                                #IMPRIME EL SGTE MENSAJE
    mostrar_mensaje(" ")                      #MANDA LA FUNCION MOSTRAR MENSAJE

def registrar():
    mostrar_mensaje("[1] REGISTRAR ALUMNO")
    dni = input("DNI    :")
    nombre = input("NOMBRE  :")
    email = input("EMAIL    :")
    dic_nuevo_alumno = {
        dni : {
                'nombre':nombre,
                'email': email
                }
    }
    dic_alumnos.update(dic_nuevo_alumno)

def mostrar():
    mostrar_mensaje("[2] MOSTRAR ALUMNOS")
    for dni,datos in dic_alumnos.items(): #ASIGNA UNA CLAVE DEL DICCIONARIO QUE ES DNI Y LUEGO ITERA CADA CLAVE-VALOR ASIGNADA AL DICCIONARIO
        print(f"DNI : {dni}")
        print(f"Nombre : {datos['nombre']}")   #ACCEDE AL VALOR CON LA CLAVE NOMBRE
        print(f"EMAIL : {datos['email']}")     #ACCEDE AL VALOR CON LA CLAVE EMAIL, SE ACCEDE AL DICCIONARIO QUE ESTA DENTRO DE DATOS QUE CONTIENE VALOR EMAIL
        mostrar_mensaje(" ")

def actualizar():
    mostrar_mensaje("[3] ACTUALIZAR ALUMNO")
    dni = input("INGRESE DNI DEL ALUMNO A ACTUALIZAR")
    if dni in dic_alumnos:
        print(f"ALUMNO A ACTUALIZAR  {dic_alumnos[dni]['nombre']}")
        nuevo_nombre = input('NOMBRE : ')
        nuevo_email = input('EMAIL :')
        dic_act_alumno = {
            dni : {
                'nombre':nuevo_nombre,
                'email':nuevo_email
            }
        }
        dic_alumnos.update(dic_act_alumno)
        print("ALUMNO ACTUALIZADO CON EXITO")

def eliminar():
    mostrar_mensaje("[4] ELIMINAR ALUMNO")
    dni = input("INGRES EL DNI DEL ALUMNO A ELIMINAR : ")
    if dni in dic_alumnos:
        dic_alumnos.pop(dni)
        print("ALUMNO ELIMINADO")
    else:
        print("NO SE ENCONTRO EL ALUMNO")