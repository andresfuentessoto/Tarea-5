#Ejercicio 1. Lambda
#(Ejercicio 1 de tarea 2)

'''Ejercicio original que devuelve el factorial de cualquier numero entero'''

#numero=int(input("Por favor ingrese un número entero"))
#factorial=1
#if numero<0:
#       print("Error número negativo, por favor ingrese un número entero")
#if numero>=0:
#    for i in range(1,numero+1):    
#        factorial=factorial*i       
#print("Factorial:",factorial) 


#Modificacion de codigo original para devolver el facotorial de un numero
'''
en este caso se importa la funcion reduce del moduloo functools
despues se le solicita el numero entero y si es negativo o fraccionado se sale
en el else se utiliza la funcion lambda que usa 'x' y 'y' para guardar los numeros del rango del factorial
despues el reduce simplifica todos los numeros de lambda y del range a uno solo, guardandolo en la variable factorial
para ya por ultimo imprimirlo
Este ejemplo funciona con cualquier numero entero que desee.
'''

from functools import reduce

numero = int(input("Por favor ingrese un número entero: "))

if numero < 0:
    print("Error: número negativo. Por favor ingrese un número entero positivo.")
else:
    factorial = reduce(lambda x, y: x * y, range(1, numero + 1))
    print("Factorial:", factorial)



#Ejercicio 2. Map y lambda
#(Ejercicio 4 de tarea 2)

'''Ejercicio original que devuelve el cuadrado de cada numero en la lista'''

#lista=[1,2,3,4,5,6,7,]
 
#print ("Lista original", lista)
 
#for i in range(0,len(lista)):
#	lista[i]=lista[i]*lista[i]*lista[i]
 
#print ("La lista al cubo es", lista)



#Ejercicio con la modificacion utilizando Map y Lambda, igual devuelve el cuadrado de los numeros en la lista

'''
En este caso esta la lista y se imprime
se utiliza la funcion lambda para que en la variable x utilice los elementos de lista
la funcion map itera la funcion lambda para que aplique la funcion al cubo en cada elemento de lista
y esta sea guardada en lista que a su vez es guardada en la variable lista_alcubo, que finalmente es impresa
Este ejemplo fue probado con la lista que muestra y agregandole cualquier otro numero
'''


lista = [1, 2, 3, 4, 5, 6, 7]

print("Lista original:", lista)

lista_alcubo = list(map(lambda x: x**3, lista))

print("La lista al cubo es:", lista_alcubo)






#Ejercicio 3. Filter'

#Ejercicio 3 de Tarea 4

'''Ejercicio original en el cual se elimina un elemento de la lista
'''
#lista = ['gato','perro','cangrejo','perro','conejo']

#for x in lista:
#    if x == 'perro':
#     lista.remove('perro')

#print (lista)

''' Aca abajo esta el ejemplo utilizando filter, en el cual esta la lista y esta la variable elemento a remover,
lambda con variable x busca los elementos en lista diferentes a la variable que esta en elementos a remover y los itera
con la funcion filtro y al haber variables(true) los guarda en list y a su vez en la variable lista y los imprime
en este ejemplo esta seleccionado perro, sin embargo, se probo tambien con conejo
'''

lista = ['gato', 'perro', 'cangrejo', 'perro', 'conejo']
elemento_a_remover = 'perro'
lista = list(filter(lambda x: x != elemento_a_remover, lista))

print(lista)  
    










#Ejercicio4. Map'
 #Ejercicio 2 de Tarea 2

'''Ejemplo original para la creacion de una 'piramide de numeros' en el cual va imprimiendo una lista sumando 1,
llegando al numero final ingresado por el usuario
'''
#numero=int(input("Por favor ingrese un número mayor a 0, gracias:")) 
#if numero<0:
#    print("Error, por favor ingrese un número mayor a 0")
#for i in range (1,numero+1):
#    for j in range (1, i+1):
#         print(j , end=" ")
#    print("") 


''' Este es otro ejemplo utilizando map, es el mismo codigo, solo la linea 18 se crea para guardar los numeros
dandoles un espacio y uniendolos con el join y convirtiendo los datos que estan en el row a string mediante el map
antes de concatenarlos (uni mas de 1 str o lista), el ejemplo funciona con cualquier numero mayor a 0
'''

numero = int(input("Por favor ingrese un número mayor a 0, gracias:"))
if numero < 0:
    print("Error, por favor ingrese un número mayor a 0")
else:
    for i in range(1, numero+1):
        row = list(range(1, i+1))
        row_str = ' '.join(map(str, row))
        print(row_str)
