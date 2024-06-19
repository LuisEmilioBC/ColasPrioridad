# Práctica de colas de prioridad de la clase 7

from ColaPrioridad import ColaPrioridad

cola = ColaPrioridad()

def intinput(string : str):
    bandera = False
    while not bandera:
        try:
            return int(input(string))
            bandera = True
        except ValueError:
            print("No es un entero válido")


opcion = 0
while opcion!=3 : 
    opcion = intinput('Ingrese la opción que requiera: \n1. Agregar Tarea\n2. Realizar Tarea\n3. Salir\nOpción : ')
    match opcion:
        case 1:
            nombre = input('Ingrese el nombre de la tarea : ')
            prioridad = intinput('Ingrese la prioridad de la tarea : ')
            cola.push(nombre, prioridad)
        
        case 2:
            print(cola.pop())