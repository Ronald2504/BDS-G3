dias = ['lunes','martes','miercoles']
print(dias)
print(dias[-2])

#AGREGAR VALORES A LA LISTA
dias.append('jueves')
dias.append('viernes')
print(dias)

#ELIMINAR UN VALOR DE LA LISTA
dias.pop(3)
print(dias)
del dias[2:4]
print(dias)
dias.append('miercoles')
dias.append('jueves')

#ACTUALIZAR UN VALOR DE LA LISTA
dias[2] = 'miercoles'
print(dias)
dias.append('viernes')

#RECORRER UNA LISTA
for dia in dias:
    print(dia)