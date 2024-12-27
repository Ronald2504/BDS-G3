# Ejercicio 1: Gestión de Inventario
# Enunciado:
# Diseña un sistema de gestión de inventario para un almacén. El sistema debe permitir las siguientes funcionalidades:
# 1. **Registrar un producto**: Ingresar el código, nombre y cantidad de un producto al inventario.
# 2. **Mostrar los productos registrados**: Mostrar el código, nombre y cantidad de todos los productos en el inventario.
# 3. **Actualizar la cantidad de un producto**: Permitir actualizar la cantidad de un producto dado su código.
# 4. **Eliminar un producto**: Eliminar un producto del inventario dado su código.
# 5. **Salir**: Guardar los cambios realizados y finalizar la ejecución del programa.
# Los datos deben ser almacenados en un archivo de texto (`inventario.txt`), y el sistema debe permitir cargar los datos desde ese archivo al iniciar y guardarlos nuevamente al finalizar.

##ENTRADA
from lib_inventario import *

cargar_inventario('inventario.txt')


##SALIDA