def sumar(n1,n2):
    resultado = n1 + n2
    return resultado

n1 = input("Ingrese nro 1 : ")
n2 = input("Ingrese nro 2 : ")
suma = sumar(int(n1),int(n2))
print(f'La suma de {n1} + {n2} es {suma}')