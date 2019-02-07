# Bootcamp

Un material sobre lo que se esta desarrollando en el bootcamp.

## VARIABLES
En programación, las variables son espacios reservados en la memoria que, como su nombre indica, pueden cambiar de contenido a lo largo de la ejecución de un programa.
#### TIP: Para que nuestro código sea más entendible y claro, el identificador o nombre de la variable debe reflejar el uso que le damos dentro del programa.

## TIPOS DE DATOS
Todos los valores que aparecen en un programa tienen un tipo. Estos son algunos tipos de datos elementales de Python.
### Números:
-Enteros (int): Los números enteros son aquellos números positivos o negativos que no tienen decimales.
Por ejemplo -3, -2, -1, 0, 1, 2, 3, etc.
#### Al asignar un número a una variable esta pasará a tener tipo int
Ejemplos:

	a=5		x= -1000		b= -62		y= 555

-Decimales(float): son los que tienen decimales. En Python se expresan mediante el tipo float. Se escribe primero la parte     entera, seguido de un punto y por último la parte decimal.

Ejemplos:

	x= 1.22  -----> el número real 1.22 se le asigna a la variable x

	a=  - 5.6 -----> el número real -5.6 se le asigna a la variable a

### Cadenas de texto (str):
A los valores que representan texto (alfanumérico) se les llama strings y tienen el tipo str. Pueden ser representados con texto entre comillas simples o comillas dobles

Ejemplos:

	“Hola Amigos”
	“Febrero”

	# Aquí asignamos la cadena “Pingüino” a la variable a

	a= “Pinguino”

### Valores booleanos (bool):
Los valores True(verdadero) y False(falso) son de tipo bool y  representan valores lógicos. Numéricamente el False equivale a 0 y cualquier otro número equivale a True pero su valor por defecto es 1.
Entonces,
* Si la expresión lógica es cierta, el resultado es True
* Si la expresión lógica NO es cierta, el resultado es False

## OPERADORES
### Operadores Aritmético

	+	Suma
	-	Resta
	*	Multiplicación
	**	Exponente
	/	División
	//	División entera
 	%	Modulo o Residuo*

#### Residuo: la operación módulo obtiene el resto de la división de un número por otro. Por ejemplo: 10%2=0 , 7%2=1

Ejemplos:

		110+15= 125 (suma)	    	3**2=9 (Potencia)		
		11/2=5.5 (División)		11//2=5 (División Entera)


### Operadores de Cadenas

	+	Concatenación
	*	Repetición


Ejemplos:

		"hola" + "mundo" = “holamundo”  (concatenación)
		“hola”*2 = ”holahola” (Repetimos la cadena “hola” dos veces)

### Operadores de relación 	
	==	a == b ¿a igual a b?
	!=	a != b ¿a distinta de b?
	>	a > b ¿a mayor que b?
	<	a < b ¿a menor que b?
	>=	a >= b ¿a mayor o igual que b?
	<=	a <= b ¿a menor o igual que b?

Ejemplos:

		"hola" == 'hola'
		True

		"hola" != 'Hola'
		True

		5 <= 3
		False

		2 * 9 == 6
		False

### Operadores lógicos

	or	a or b  (¿Se cumplen a o b?)
	and	a and b (¿Se comple a y b?)
	not	not x   (Contrario a x)

### Operadores de asignación
Los operadores de asignación se utilizan para enlazar un valor con una variable. El más común es:

	=	Asignación simple


Ejemplo:

		x= “Benito Pérez”  	(Asigna el tipo de dato str a la variable x)

## FUNCIONES

Una función es un bloque de código con un nombre asociado, que puede recibir argumentos como entrada, que realiza una serie de tareas y puede devolver un valor. Este bloque puede ser llamado cuando se necesite.
Si necesitamos crear nuestra propia función tenemos que definirla, para eso usamos La sentencia def

#### OJO: La definición de una función no ejecuta el cuerpo de la función; esto es ejecutado solamente cuando la función es llamada.


La sintaxis para una definición de función en Python es:

	def nombre_de_la_funcion (PARAMETRO):
		SENTENCIAS
		return EXPRESION

* PARÁMETRO: son los datos o la información que recibe la función
* SENTENCIAS, es el bloque de sentencias en código que realiza cierta operación.
* return ,  El valor que va a devolvernos la función una vez que la llamemos.
* EXPRESION, es la expresión o variable que devuelve la sentencia return.

Ejemplo:

	# Definir una función que reciba dos números enteros, los sume y luego retorne la suma.

	def sumar(valor1,valor2):
		sum=valor1+valor2
		return sum

	#Llamar a la función definida anteriormente para sumar los números 3 y 7 y guardar eso en una variable llamada A

	A=sumar(3,7)

	#Entonces A adquiere el valor de 3+7

	A=10


Tambien existen funciones que vienen incluidas en el lenguaje, tales como:

* print() ----> imprime en pantalla lo que pongamos dentro de los paréntesis.

	Por ejemplo:

		print(“Mi remera es azul”)
* len() ----> devuelve la longitud del dato que se introduzca dentro de los paréntesis.
	Por ejemplo:

		len(“Villa Florida”) = 13  


		#Si tenemos una lista llamada nombres

		nombres=[Maria, Pedro, Juan, Meli]
		len(nombres)=4

## LISTAS
son una estructura de datos y un tipo de dato con características especiales. Lo especial de las listas en Python es que nos permiten almacenar cualquier tipo de valor como números enteros, números decimales, cadenas y hasta otras listas;

#### Una lista debe tener nombre luego un = y corchetes. Dentro de los corchetes se especifican los elementos separados por comas

	lista=[element1, element2,...]

por ejemplo:

	muestra = [1, 2.5, “Aleluya”, [5,6] ]

	#Si quiero acceder a elementos en una posición específica lo hacemos poniendo el nombre de nuestra lista y dentro del corchete el índice.

	muestra[0]   es  1
	muestra[1]   es 2.5
	muestra[2]  es “Aleluya”
	muestra[3]  es [5,6]
	muestra[3][0]  es 5
	muestra[3][1]  es 6

* Append(): nos permite agregar nuevos elementos a una lista, al final de ella

		muestra.append(10)   es  [1, 2.5, “Aleluya”, [5,6],10 ]
		muestra.append([2,5]) es [1, 2.5, “Aleluya”', [5,6], 10, [2,5] ]



## CICLOS O LOOPS:
El bucle while se ejecutara repetidamente un bloque de codigo mientras su expresión condicional sea verdadera.

	while condicion:
		# bloque de codigo

El ciclo for repite el bloque de instrucciones un número predeterminado de veces. El bloque de instrucciones que se repite se suele llamar cuerpo del bucle

La sintaxis de un bucle for es la siguiente:

	for variable in lista:   
		# cuerpo del bucle


* variable : es una variable de control que va tomando el valor de cada elemento de lista.

#### OJO: se pueden también hacer for in cadenas, for in ranges, etc

## CONDICIONALES

* if: permite que un programa ejecute unas instrucciones cuando se cumplan una condición.

		if condición:
			# aquí van las órdenes que se ejecutan si la condición es cierta y que pueden ocupar varias líneas

* else: es lo que se va a ejecutar en caso de que no se cumpla la condición del if

Ejemplo:


	x=100
	if x % 2 == 0:
		print (x,"es par")
	else:
		print (x, "es impar")

#
hhh
