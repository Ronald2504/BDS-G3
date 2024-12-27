#DEBO DE INGRESAR A UN ARCHIVO DONDE DEBA DE ABRIR, LEER Y GUARDAR
#LA INFORMACION EN UN VARIABLE, LA INFORMACION DE LA VARIABLE DEBO
#DE SEPARARA EN LINEAS PARA LUEGO SEPARAR EN COMAS Y ASI 
# CADA LINEA ALAMCENARLA EN UN 
#DICCIONARIO Y ASI ESTE DICCIONARIO ACTUALIZARLO

dic_inventario = {}

def cargar_inventario(file_name):
    file = open(file_name,'r')
    str_inventario = file.read()
    file.close()
    lista_inventario = str_inventario.splitlines()
    for str_fila in lista_inventario:
        lista_fila = str_fila.split(',')
        dic_fila = {
            'nombre': lista_fila[1],
            'cantidad' : lista_fila[2]
        }
        dic_nuev_inventario = {
            lista_fila[0]: dic_fila
        }
        dic_inventario.update(dic_nuev_inventario)

def registrar():
    "[1] REGISTRAR ALUMNO"
    codigo = input("Codigo: ")
    nombre = input("NOMBRE: ")
    cantidad = input("CANTIDAD: ")
    dic_nuev_inventario = {
        codigo: {
            'nombre': nombre,
            'cantidad': cantidad
        }
    }
    dic_inventario.update(dic_nuev_inventario)

def mostrar():
    for codigo,datos in dic_inventario.items:
        print(f"CODIGO: {codigo}")
        print(f"NOMBRE: {nombre}")
        print(f"CANTIDAD: {cantidad}")

def actualizar():
    codigo = input("INGRESE CODIGO A ACTUALIZAR")
    if codigo in dic_inventario:
        print(f"ALUMNO A ACTUALIZAR {dic_inventario[codigo]['nombre']}")
        nuevo_nombre= input("INGRESE NOMBRE: ")
        nueva_cantidad= input("INGRESE CANTIDAD: ")
        dic_act_inventario = {
            codigo: {
                'nombre': nuevo_nombre,
                'cantidad': nueva_cantidad
            }
        }
        dic_inventario.update(dic_act_inventario)
    
def eliminar():
    codigo = input("INGRESE EL CODIGO A ELIMINAR: ")
    if codigo in dic_inventario:
        dic_inventario.pop()





































dic_inventario = {}
print("""
        [1] REGISTRAR PRODUCTO
        [2] MOSTRAR PRODUCTO
        [3] ACTUALIZAR PRODUCTO
        [4] ELIMINAR PRODUCTO
        [5] SALIR
        """)
opcion=int(input("Coloque la opcion a realizar: "))

if opcion == 1:
    print("""
          ==================
          REGISTRAR PRODUCTO
          ==================
          """)
    codigo=input("CODIGO:  ")
    nombre=input("NOMBRE:  ")
    cantidad=input("CANTIDAD:  ")
    dic_nuev_inventario = {
        codigo :{
            'nombre': nombre,
            'cantidad': cantidad
        }
    }
    dic_inventario.update(dic_nuev_inventario)
    print(dic_inventario)
    