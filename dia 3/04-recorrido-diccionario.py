capitales = {
        'Peru': 'Lima',
        'Ecuador': 'Quito',
        'Chile': 'Santiago',
        'Colombia':'Bodega'
    }

print('=' * 50 + "RECORRIDO POR CLAVES") 
#RECORRIDO POR CLAVES
for clave in capitales.keys():
    print(clave)
    
print('=' * 50 + "RECORRIDO POR VALORES") 

#RECORRIDO POR VALORES
for valor in capitales.values():
    print(valor)

print('='*50 + "RECORRIDO POR CLAVE, VALOR")

#RECORRIDO POR CLAVE, VALOR
for clave,valor in capitales.items():
    print(f'La capital de {clave} es {valor}')    
