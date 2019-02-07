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

	#Aquí asignamos la cadena “Pingüino” a la variable a 
	
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

	#Ejemplos:
		110+15= 125 (suma)	    	3**2=9 (Potencia)		
		11/2=5.5 (División)		11//2=5 (División Entera)



### Operadores de Cadenas	
	
	+	Concatenación
	*	Repetición


	#Ejemplos: 
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

Operadores lógicos	Evalúa
or	a or b    (¿Se cumplen a o b?)
and	a and b (¿Se comple a y b?)
not	not x      (Contrario a x)

Operadores de asignación.
Los operadores de asignación se utilizan para enlazar un valor con una variable. El más común es: 
=	Asignación simple

Ejemplo:
x= “Benito Pérez”  	(Asigna el tipo de dato str a la variable x)

