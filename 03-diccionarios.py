#tipos de datos
#Diccionarios
#mutables
#elementos no ordenados
#{Clave:Valor}

diccionario_productos = {"nombre":"manzana","valor":20.00,"stock":250}
print(type(diccionario_productos))
print(diccionario_productos)

print(len(diccionario_productos))


#cambiar valores
diccionario_productos["valor"] = 15.00
print(diccionario_productos)

#elimina valores
del diccionario_productos["stock"]
print(diccionario_productos)


#tipo de datos
print(type(diccionario_productos["nombre"]))