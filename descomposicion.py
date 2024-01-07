"""
Ingresando un numero entero positivo, lo descompone 
en unidades, decenas, centenas, etc
"""
while True:
    numero = int(input("Ingrese un numero entero positivo: "))
    if numero<=0:
        continue
    else:
        break

cadena = str(numero)
digitos = len(cadena)
dig = len(cadena) -1

for cad in cadena:
    num = int(cad)*(10**dig)
    print(f"{num:0{digitos}d}")
    dig -= 1