#tipos de datos
#tuplas
#inmutables
#no crud

tuplas_familia = ("William", "Alexiis", "Gabriela")
print(type(tuplas_familia)) 
print(tuplas_familia)
print(len(tuplas_familia))
# tuplas_familia.pop() error 

#tupla a lista
tupla = (1, 2, 3, 4, 5, 6)
print(tupla)
print(type(tupla))

lista = list(tupla)
print(lista)
print(type(lista))

#lista a tupla
lista = ["William", "Alexis", "Herrera"]
print(lista)
print(type(lista))

tupla = list(lista)
print(tupla)
print(type(tupla))

#editando valores de tuplas
paises_latinoamerica = ("colombia", "venezula", "chile", "bolivia", "españa")
paises_latinoamerica = list(paises_latinoamerica)
paises_latinoamerica.remove("españa")
paises_latinoamerica = tuple(paises_latinoamerica)
print(paises_latinoamerica)
