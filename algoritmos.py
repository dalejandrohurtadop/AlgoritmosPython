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
                
def es_primo01(n):
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

def es_primo02(n):
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
    
#14. Escriba un programa en Python que imprima los números primos del 1 al 100.
    
def lista_primos(n):
    lista = [num for num in range(1,n+1) if es_primo02(num)]
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
    
#5. Escriba un programa en Python que lea un número entero y determine si es perfecto.
    
def divisores_primos(n):

    n_medios = int(round(n/2,0) + 2)

    divisores = [i for i in lista_primos(n_medios) if n%i == 0]
       
    factores = []

    for j in divisores:
        a = [j,0]
        num = n

        while num%j == 0:
            a[1] = a[1] + 1
            num = num/j

        factores.append(a)

    return divisores, factores


def divisores(n):

    n_medios = int(round(n/2,0) + 2)
    divisores = [i for i in range(1,n_medios) if n%i == 0]
       
    return divisores


def es_num_perfecto(n):

    if sum(divisores(n)) == n:
        result = str(n)+" Es número perfecto"
    else:
        result = str(n)+" No es número perfecto"

    return result



   
inicio = time.time()

n=496
divisores_primo, factores = divisores_primos(n)


print(divisores_primo)
print(factores)
print(divisores(n))
print(es_num_perfecto(n))


time.sleep(1)
# -------------

fin = time.time()
print(fin-inicio)

     

