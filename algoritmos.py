#Archivo: algoritmos.py
#Autor: Alejandro Hurtado
#Fecha: Diciembre de 2023
#Descripción: Contempla la solución de erjicios basicos de algoritmos
#enumerados según el docuemtno de enunciados: enunciados.txt


import time

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




inicio = time.time()

n = 100

print(lista_impares(n))


time.sleep(1)
# -------------

fin = time.time()
print(fin-inicio)

     

