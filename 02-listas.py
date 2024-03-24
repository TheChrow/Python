#tipos de datos
#mutables

#listas 
lista_alumnos = ["william", "Kevin", 25, True] 
print(type(lista_alumnos))

#funciones listas

lista_alumnos.append("William") #agregar
print(lista_alumnos)

lista_alumnos.pop() #Eliminar
print(lista_alumnos)

lista_alumnos.insert(1,"Alexa") #agregar (indice,Valor)
print(lista_alumnos)

print(lista_alumnos.index("Alexa")) #posiicion elementos

lista_alumnos.remove("william") #remueve elemento
print(lista_alumnos)

#cantidad elememntos en lista
print(len(lista_alumnos)) 

#Union lista
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8, 9]
lista3 = lista1 + lista2
print(lista3)

#repetir valores en lista
lista4 = [1] * 10
print(lista4)