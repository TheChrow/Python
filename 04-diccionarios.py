#tipos de datos
#Diccionarios
#mutables
#elementos no ordenados
#{Clave:Valor}

diccionario_productos = {"nombre":"manzana","valor":20.00,"stock":250}
print(type(diccionario_productos))
print(diccionario_productos)

#cantidad elementos
print(len(diccionario_productos))

#cambiar valores
diccionario_productos["valor"] = 15.00
print(diccionario_productos)

#elimina valores
del diccionario_productos["stock"]
print(diccionario_productos)

#tipo de datos
print(type(diccionario_productos["nombre"]))

#tuplas claves diccionario

datos_persona = ("nombre", "edad", "fecha_nacimiento")
lista_empleados = {datos_persona[0]:"William", datos_persona[1]:30, datos_persona[2]:"1993/29/03"}

print(lista_empleados)

#diccionarios anidados
inventario_led = {

    "producto1":{"id": "01",
     "sku": "N10100100",
     "stock": 255,
     "precio": 25000,
     "estado": "linea",
    },

    "producto2":{"id": "02",
     "sku": "C10200103",
     "stock": 55,
     "precio": 35000,
     "estado": "desactivado"
    }
}

inventario_led["producto3"] = {
    "id":"03",
    "sku":"C10300103",
    "stock":66,
    "precio":25000,
    "estado":"desactivado",
    }

print(inventario_led)
print(len(inventario_led))

#agregar productos
print(inventario_led["producto1"]["precio"])

#items()
#usado en diccionarios
#regresa una vista iterable
#podemos acceder a sus elementos de forma secuencial 
for clave, valor in inventario_led.items():
    print(f"{clave}:{valor}")