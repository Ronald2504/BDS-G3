print("MI CALCULADORA")
#ENTRADA
numero1 = input("Numero 1: ")
numero2 = input("Numero 2: ")
operacion = input("¿Que operacion matematica desea hacer? (suma,resta,multiplicacion,division): ")
#PROCESO
if (operacion == "suma"):
    resultado = int(numero1) + int(numero2)
elif (operacion == "resta"):
    resultado = int(numero1) - int(numero2)
elif (operacion == "multiplicacion"):
    resultado = int(numero1) * int(numero2)
elif (operacion == "division"):
    resultado = int(numero1) / int(numero2) 
else:
    print("La operacion no existe!")
    exit()
#SALIDA
print(f"La {operacion} de {numero1} y {numero2} es {resultado}")