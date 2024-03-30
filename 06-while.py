numero = int(input("Ingrese un numero para validar si es par: "))
numero_resultado = numero % 2
intetos = 0
contador_intetos = 3

while numero_resultado != 0:
    if numero_resultado > 0:
        print(f"{numero}: Este numero no es par") 
        numero = int(input("Ingrese nuevamente un numero: "))
        intetos = intetos + 1

        contador_intetos = contador_intetos-1
        print(f"Intetos restantes: {contador_intetos}")

    if intetos > 2:
        print("Ha consumido todos sus intetos")
        break

if numero_resultado == 0:
    print(f"{numero}: Numero es par")

