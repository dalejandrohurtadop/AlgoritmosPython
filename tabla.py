import sys
if len(sys.argv) ==3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    if filas < 1 or filas > 9 or columnas <1 or columnas >9:
        print("Filas o columans incorrectas")
    else:
        for f in range(filas):
            print("\n")
            for c in range(columnas):
                print(" * ", end = "")
else:
    print("Error, argumentos incorrectos")
    print("Ejemplo: Tabla.py [1-9] [1-9]")
