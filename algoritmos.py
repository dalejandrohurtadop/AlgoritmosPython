# 1. Escriba un programa en Python que imprima la siguiente secuencia del eneunciado correspondiente

def secuencia_escalonada(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print("\n")

#2. Escriba un programa en Python que imprima los números pares del 1 al 100.

def numero_pares(n):
    pares = [num for num in range(1,n+1) if num%2 == 0]
    return pares

# 3. Escriba un programa en Python que imprima la siguiente secuencia del eneunciado correspondiente

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
        

        
secuencia_ordenada_escalonada(120)