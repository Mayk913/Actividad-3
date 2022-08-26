# Generar un menu, con N opciones, cominando diccionarios con tuplas, que permita colocar el valor de la opción, 
# la descripcion de opción y el nombre de al función que ejecutaria dicha opción.
lista=[]
##
noptions=int(input("Cuantas opcines desea ingresar:"))
###

def add():
    descripcion=input("Redacte la descripcion de la funcion:")
    nombre=input("Digite el nombre de la funcion: ")
     d = {
    "Nombre de la funcion: " + nombre,
    "Descripcion de la funcion: "+ descripcion
    }
    tupla =(d)
    lista.append(tupla)