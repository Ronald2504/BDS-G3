# TUPLAS: IGUAL A LISTAS PERO INMUTABLES
dias = ('lunes','martes','miercoles','jueves')
print(dias)
print(type(dias))

#PARA AGERGAR DATOS CONVERTIMOS LA TUPLA EN LISTA
dias=list(dias)
print(type(dias))
dias.append("viernes")
dias = tuple(dias)
print(type(dias))

#RECORRER UNA LISTA
for dia in dias:
    print(dia)