import csv

try:
    with open('videojuegos.csv', newline='') as archivo:
        lector = csv.reader(archivo)
        encabezado = next(lector)  # Leer y guardar cabecera
        print(f"{encabezado[0]:<25} {encabezado[1]:<15} {encabezado[2]:<6} {encabezado[3]}")
        print("-" * 60)
        for fila in lector:
            titulo, genero, anio, plataforma = fila
            print(f"{titulo:<25} {genero:<15} {anio:<6} {plataforma}")
except FileNotFoundError:
    print(" El archivo 'videojuegos.csv' no se encuentra. Primero corre el programa escritor.")
