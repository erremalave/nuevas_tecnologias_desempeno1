#https://blog.hubspot.es/website/lista-python
#Las listas son estructuras de datos lineales
#Se crean usando brackets je: my_list = []
#Las listas son ordenadas (orende de inserción) estoy quiere decir que el ultimo dato ingresado ocupara la ultima posición
#Emplea metodos para manilupar los items de la misma
#Como los array la primera posicion inicia en 0
#Permite items duplicados
#Las listas son mutables, es decir podemos agregar, actualizar o remover items
#Puede contener distintos tipos de datos

nombre = ["Pepito", "Andres", "Juan", "Maria", "Pedro"]
edad = [25, 19, 21, 33, 40]
estatura = [1.80, 1.65, 1.74, 1.66, 1.54]
casado = [False, False, False, True, True]
usuario = ["Pepito", 25, 1.80, False]

print(len(edad))

print(type(nombre))
print(type(edad))
print(type(estatura))
print(type(casado))
print(type(usuario))

#Slice --- rangos en la lista

print(usuario[0:3])
print(nombre[1:3])
print(nombre[:3])
print(nombre[1:])
print(nombre[:-1])
print(nombre[:4])
print(nombre[-4:-1])
print(nombre[1:4])

#Podemos validar si existe en la lista algun elemento
# f delante permite concatenar de forma ágil

if "Pepito" in nombre:
    print("el nombre esta en la lista")
else:
    print("No se encontró el nombre buscado")

usuario[0] = "Luis"

nombre[0:3] = "Manuel", "Jorge", "Andrea"
print(nombre[0:5])

#insertar un item en una posición especifica => insert (i, value) el insert recibe dos parametros, la ubicacion y el valor

nombre.insert(0, "Pepito")
print(nombre[0:])

#para insertar items al final de la lista se utiliza el metodo append()

nombre.append("Laura")
print(nombre[0:])


#con el metodo extend podemos agregar una lista a otra lista

nombre2 = ["Ricardo", "Erre"]
nombre.extend(nombre2)
print(nombre)

#quitar elementos de una lista con los metodos remove(value) o pop(i)

nombre.remove("Erre")
print(nombre[0:])

nombre.pop(4)
print(nombre[0:])

#eliminar un elemento de la lista con el funcion del

del nombre[1]
print(nombre[0:])

#con el metodo clear vacía la lista pero no elimia los datos guardados

nombre.clear()

#si usamos la funcion del sin especificar un valor, se elimina la lista
del nombre
#print(nombre[0:])

#recorriendo lista

for i in edad:
    print(i)

#iterar en los index

for i in range(len(estatura)):
    print(estatura[i])


#list comprehension

print("-------------------")

[print(x) for x in edad]

print("-------------------")

#iterar la lista usando un while

i = 0

while i < len(usuario):
    print(usuario[i])
    i += 1


#enumerate

print("-------------------")

for i, edad in enumerate(edad):
    print(i, edad)

print("-------------------")

# dos listas ingresos y egresos, se pueden hacer retiros pero no pueden quedar en negativo, se tiene que imprimir el saldo constantemente
# cuando se retire dinero y cuando se deposite dinero 