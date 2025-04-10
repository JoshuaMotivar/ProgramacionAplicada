import csv

videojuegos = []

while True:
    entrada = input("Ingrese los datos del videojuego (Título, Género, Año, Plataforma) separados por comas, o 'salir' para terminar: ")
    if entrada.lower() == 'salir':
        break
    try:
        titulo, genero, anio, plataforma = entrada.split(',')
        videojuegos.append([titulo.strip(), genero.strip(), int(anio.strip()), plataforma.strip()])
    except ValueError:
        print("Entrada inválida. Asegúrese de usar el formato correcto: Título, Género, Año, Plataforma")

with open('videojuegos.csv', 'w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Título', 'Género', 'Año', 'Plataforma'])  # Cabecera
    escritor.writerows(videojuegos)

print(" Datos guardados exitosamente en videojuegos.csv")
