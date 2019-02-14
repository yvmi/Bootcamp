##################
# Variables
##################

# Asignar una variable entera (integer)
numero = 42

# Asignar una variable cadena (string)
cadena = "Hola Mundo"

# Asignar una variable decimal (float)
decimal = 42.0

# Asignar una variable booleana (bool)
booleano = True # Puede ser True o False

# Asignar una variable lista (list)
lista = [10.0, "Penguin", 442]

# Asignar una variable lista en una lista
listota = [[12, 5], ["ay", "mama", lista]]

##################
# Operadores
##################
# Operadores aritmeticos
suma = numero + decimal
resta = suma - decimal
division = 80 / 2
multiplicacion = resta * 5
exponente = 18 ** 2
modulo = 45 % 2 # El operador modulo obtiene el resto de la división de un número por otro.

# Operadores de cadenas
concatenacion = "Hola" + "Que tal" # seria "HolaQue tal"
repeticion = "Bla" * 2 # seria "BlaBla"

# Operadores de relacion
A == X # Es A igual a X?
5 != 8 # Es 5 distinto a 8?
100 > 2 # Es 100 mayor que 2?
numero < suma # Es numero menor a suma?

# Operadores logicos
a or b    #  ¿Se cumplen a o b?
opcion1 and opcion2 # ¿Se cumplen opcion1 y opcion2?

# Operador de asignacion
asign = 54 # Asignamos valor 54 a la variable asign

##################
# Funciones
##################
# Definir una Funcion que reciba dos cadenas y retorne una sola cadena
def nombre_completo (nombre, apellido):
    completo = nombre + " " + apellido # se debe sumar un espacio en blanco
    return completo

nombre_completo("Ada", "Lovelace") # para que imprima Ada Lovelace

##################
# Ciclos
##################
# Recorremos la lista participantes, e imprimir cada elemento de la lista.
participantes = ["Benito", "Pepe", "Laura", "Leila"]
for alumnos in participantes:
    print (alumnos)

# Ciclo while
a = 0
while a < 10 :
    a=a+1

##################
# Condicionales
##################
# Condicional if y else
if hora == 12:
    print ("Es hora de comer!!")
else:
    print ("Come alambre")

# Condicional if , elif y else
pelota = "roja"
if pelota == "verde":
    print ("La pelota es verde")
elif pelota == "roja":
    print ("La pelota es roja")
elif pelota == "azul":
    print ("La pelota es azul")
else:
    print ("No se que color es la pelota")

##################
# Clases
##################
# Definir una Clase
class Persona():
    def __init__(self, nombre = " ", edad = 0, cabello = " "):
        self.name = nombre
        self.age = edad
        self.hair = cabello

    def cumpleanos(self):
        new_age = self.age + 1
        return new_age

    def tenhido(self, color):
        self.hair = color
        new_color = self.hair
        return new_color

# Creamos el objeto persona1
persona1 = Persona("Leo", 16, "Negro")
# Imprime la edad actual de persona1
print(persona1.age)
# llamamos al metodo cumpleanos
edad_final = persona1.cumpleanos()
# imprime la nueva edad_final
print(edad_final)
# Imprime el color de cabello de persona1
print(persona1.hair)
# llamamos el metodo tenhido
nuevo_look = persona1.tenhido("Verde")
# imprime el nuevo color de cabello
print(nuevo_look) 
