#Archivo: algoritmos.py
#Autor: Alejandro Hurtado
#Fecha: Diciembre de 2023
#Descripción: Contempla la solución de erjicios basicos de algoritmos
#enumerados según el docuemtno de enunciados: enunciados.txt


import time
import random

# 1. Escriba un programa en Python que imprima la siguiente secuencia del enunciado correspondiente

def secuencia_escalonada(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print("\n")

#2. Escriba un programa en Python que imprima los números pares del 1 al 100.

def numero_pares(n):
    pares = [num for num in range(1,n+1) if num%2 == 0]
    return pares

# 3. Escribe un programa en Python que imprima la siguiente secuencia del enunciado correspondiente

def secuencia_ordenada_escalonada(n):
    max_fila = 0
    k = 0
    j = 1
    while j <= n :
        k+=1
        max_fila = max_fila + k
        
        for i in range(k):
            if j>n:
                print("\n")
                break
            elif j == max_fila:
                print(j)
                j=j+1
            else:
                print(j, end=" ")
                j=j+1
        
#4. Escriba un programa en python que lea un número entero y determine si es primo.
                
def es_primo02(n):
    n_medios = int(round(n/2,0) + 2)

    if (n == 3) | (n ==2):
        return print("El numero ", n, " es primo")
    elif n%2 == 0 | n == 1:
        print("El numero ", n, " no es primo")
    else:
        for i in range(2, n_medios, 1):
            if(n%i == 0 ):
                return print("El numero ", n, " no es primo"), print("Tiene como factor común el número  :", i) 
        return print("El numero ", n, " es primo")

def es_primo01(n):
    n_medios = int(round(n/2,0) + 2)

    if (n == 3) | (n ==2):
        return True
    elif n%2 == 0 | n == 1:
        return False
    else:
        for i in range(2, n_medios, 1):
            if(n%i == 0 ):
                return False 
        return True
    
#5. Escriba un programa en Python que lea un número entero y determine si es perfecto.
    
def divisores_primos(n):
    
    num = n
    while num%2 == 0:
        num = num/2

    n_medios = int(round(num/2,0) + 2)

    divisores = [i for i in lista_primos(n_medios) if n%i == 0]
       
    factores = []

    for j in divisores:
        a = [j,0]
        num = n

        while num%j == 0:
            a[1] = a[1] + 1
            num = num/j

        factores.append(tuple(a))

    return divisores, factores


def divisores(n):

    n_medios = int(round(n/2,0) + 2)
    divisores = [i for i in range(1,n_medios) if n%i == 0]
       
    return divisores


def es_num_perfecto(n):

    if sum(divisores(n)) == n:
        result = True # str(n)+" Es número perfecto"
    else:
        result = False #str(n)+" No es número perfecto"

    return result

#6. Escriba un programa en Python que lea un número entero y determine si es capicúa.

def es_capicua(n):
    num = str(n)
    reverse_num = num[::-1]

    if num == reverse_num:
        return True
    else:
        return False
    
#Los siguientes enunciados se resulven con el siguiente programa
#7. Escriba un programa en Python que lea un número entero y determine si es divisible por 3.
#8. Escriba un programa en Python que lea un número entero y determine si es divisible por 5.
#9, Escriba un programa en Python que lea un número entero 'a' y un número 'n' y determine si 'a' es divisible por 'n'.

def es_divisible(a, n):
    if a%n ==0:
        return True
    else:
        return False

#10. Leer un número entero y mostrar si es par o impar.
def es_par(n):
    if n%2 ==0:
        return True
    else:
        return False
        
#11. Escriba un programa en Python que imprima la siguiente secuencia:
#	1, 4, 9, 16, 25, ..., 100

def lista_sec_imp(n):

    lista = [1]
    num = 1
    sec = lista[0]

    while sec <= n:
        num = num + 2 
        sec += num
        if sec > 100:
            break
        else:
            lista.append(sec)

    return lista

#12. Escriba un programa en Python que imprima los números pares del 1 al 100.

def lista_pares(n):
    lista = [i for i in range(1,n+1,1) if i%2 == 0]
    return lista

#13. Escriba un programa en Python que imprima los números impares del 1 al 100.

def lista_impares(n):
    lista = [i for i in range(1,n+1,2) if i%2 != 0]
    return lista

#14. Escriba un programa en Python que imprima los números primos del 1 al 100.
    
def lista_primos(n):
    lista = [num for num in range(1,n+1) if es_primo01(num)]
    return lista

def es_primo03(n):
    n_medios = int(round(n/2,0) + 2)

    if (n%2 == 0) | (n == 1):
        return False
    elif (n ==3) | (n==2):
        return True
    elif n_medios<=100000:
        lista = lista_primos(n_medios)
        for i in lista:
            if n%i == 0:
                return False 
        return True
    else:
        lista = lista_primos(100000+1) + list(range(100000,n_medios,2))
        for i in lista:
            if n%i == 0:
                return False 
        return True
    
def es_primo04(n):
    n_medios = int(round(n/2,0) + 1)

    if (n%2 == 0) | (n == 1):
        return False
    elif (n ==3) | (n==2):
        return True
    else:     
        lista=[num5 for num5 in [num3 for num3 in [num2 for  num2 in range(2, n_medios+1) if num2%2!=0] if num3%3!=0] if num5%5!=0]
        lista.insert(0,3)
        lista.insert(1,5)
        for i in lista:
            if(n%i == 0 ):
                return False 
        return True

#15. Escriba un programa en Python que imprima la siguiente secuencia:
#	*
#	**
#	***
#	****
#	*****

def sec_asteriscos(n):

    for i in range(1,n+1):
        print("*"*i)

#16. Escriba un programa en Python que imprima la siguiente secuencia:
#	1
#	2 2
#	3 3 3
#	4 4 4 4

def sec_number_triangualr(n):

    for i in range(1,n+1):
        j=str(i)+" "
        print(j*i)

# 17. Escriba una función en Python que calcule el factorial de un número.

def n_factorial(n):
    if n==1:
        return 1
    else:
        n = n * n_factorial(n-1)
        return n

#18. Escriba una función en Python que calcule la suma de los elementos de una lista.

def sum_lista(lista):
    n = int(len(lista))
    i = 0
    suma = lista[0]

    if i == n-2:
        suma = lista[i] + lista[i+1]
    else:
        suma = suma + sum_lista(lista[i+1:n])
        
    return suma

## Generar de lista con numeros aleatorios

def lista_randon(n,a,b):

    return [random.randint(a, b) for i in range(n)]

#19. Escriba una función en Python que calcule el promedio de los elementos de una lista.

def promedio_lista(lista):
    return sum(lista)/len(lista)


#20. Escriba un programa en Python que lea una lista de números enteros y determine si está ordenada de forma creciente.

def es_lista_ordenada(lista):
    n=len(lista)
    verificacion = [1 if lista[i]<=lista[i+1] else 0 for i,v in enumerate(lista[:n-1])]

    suma = sum(verificacion)

    if suma ==n-1:
        return True
    else:
        return False
    
#21. Escriba un programa en Python que lea una lista de números enteros y determine si hay números repetidos.
def num_repetido(lista):
    n_list = len(lista)
    conjunto = set(lista)
    n_set = len(conjunto)

    if n_list > n_set:
        return True
    else:
        return False

#22. Escriba un programa en Python que lea una lista de números 
#enteros y determine si hay un número que aparezca más de la mitad de las veces.

def num_rep_lista(lista):

    cantidad_elementos = len(lista)

    new_lista = list(set(lista)) #Lista de elementos no repetido
    
    #lista de elemntos no repetidos y cantidad de veces que se repiten en la lista
    num_elementos = [[j, lista.count(j)] for j in new_lista]

    #numero mayor de repeticiones
    maximo_rep = max([lista.count(j) for j in new_lista ])

    #Lista de elementos que mas se repiten, con su numero de apariciones
    valor_rep = [j for j in num_elementos if j[:][1] == maximo_rep]

    if maximo_rep >=cantidad_elementos/2:
        val_logico = True
    else:
        val_logico = False

    return valor_rep, val_logico


#23. Escriba un programa en Python que lea una lista de números enteros 
#y determine si hay un número que aparezca en dos posiciones consecutivas.

def consecutivos_val(lista):

    for i, val in enumerate(lista[:-1]):
        if lista[i] != lista[i+1]:
            val_logico = False
        else:
            val_logico = True
            break

    
    return val_logico



inicio = time.time()

n = 3
a = 2
b = 50
lista1 = lista_randon(n,a,b)
lista2 =list(range(n))
lista3 = [1,2,2,1,3,1,4,1,5,1,6,1]

print(lista3)
print(consecutivos_val(lista3))





time.sleep(1)
# -------------

fin = time.time()
print(fin-inicio)

     

