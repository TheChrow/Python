tablasMultiplicar = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]

numero = int(input("ingrese un numero a multiplicar"))

for i in tablasMultiplicar:
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")
    