#parametros args y kwards
def sumar_infinito(*args):
    resultado = 0
    for numero in args:
        resultado = resultado + numero
    return resultado


suma1 = sumar_infinito(1,3,4)
print(suma1)
suma2 = sumar_infinito(1,2)
print(suma2)

def calculadora(**kwards):
    ope = kwards.get('ope')
    n1 = kwards.get('n1')
    n2 = kwards.get('n2')
    
    if ope == "suma":
        resultado = n1 + n2
        print(f'La {ope} de {n1} + {n2} es {resultado}')
    elif ope == "resta":
        resultado = n1 - n2
        print(f'La {ope} de {n1} - {n2} es {resultado}')
    elif ope == "multiplicacion":
        resultado = n1 * n2
        print(f'La {ope} de {n1} * {n2} es {resultado}')
    elif ope == "division":
        resultado = n1 / n2
        print(f'La {ope} de {n1} / {n2} es {resultado}')       
        
        
    else:
        print('no se encontro la oepracion solicitad')


calculadora(n1=5,n2=10,ope='suma')
calculadora(ope='resta',n1=3,n2=1)
calculadora(ope='multiplicacion',n1=10,n2=15)
calculadora(ope='division',n1=10,n2=2)