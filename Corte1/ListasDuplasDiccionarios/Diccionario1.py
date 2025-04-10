# Sección 1: Diccionarios básicos
def mostrar_diccionarios_basicos():
    sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
    print(sensors)

    num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
    print(num_cameras)

    translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}
    print(translations)


# Sección 2: Diccionarios anidados y vacíos
def mostrar_diccionarios_anidados_y_vacios():
    children = {
        "von Trapp": ["Johannes", "Rosmarie", "Eleonore"],
        "Corleone": ["Sonny", "Fredo", "Michael"]
    }
    print(children)

    my_empty_dictionary = {}
    print(my_empty_dictionary)


# Sección 3: Agregar y modificar valores
def modificar_diccionarios():
    menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
    print("Before:", menu)
    menu["cheesecake"] = 8
    print("After:", menu)

    animals_in_zoo = {"horses": 2}
    print(animals_in_zoo)

    sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
    print("Before:", sensors)
    sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
    print("After:", sensors)

    user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
    print(user_ids)
    user_ids.update({"theLooper": 138475, "stringQueen": 85739})
    print(user_ids)


# Sección 4: Sobrescribir valores
def sobrescribir_valores():
    menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
    print("Before:", menu)
    menu["oatmeal"] = 5
    print("After:", menu)

    oscar_winners = {
        "Best Picture": "La La Land",
        "Best Actor": "Casey Affleck",
        "Best Actress": "Emma Stone",
        "Animated Feature": "Zootopia"
    }
    print("Before:", oscar_winners)
    oscar_winners.update({"Supporting Actress": "Viola Davis"})
    print("After1:", oscar_winners)
    oscar_winners["Best Picture"] = "Moonlight"
    print("After2:", oscar_winners)


# Sección 5: Crear diccionarios con zip() y comprensión
def crear_diccionarios_con_zip():
    names = ["Jenny", "Alexus", "Sam", "Grace"]
    heights = [61, 70, 67, 64]
    students = {key: value for key, value in zip(names, heights)}
    print(students)

    drinks = ["espresso", "chai", "decaf", "drip"]
    caffeine = [64, 40, 0, 120]
    drinks_to_caffeine = {key: value for key, value in zip(drinks, caffeine)}
    print(drinks_to_caffeine)


# Sección 6: Diccionario de canciones y biblioteca musical
def canciones_y_biblioteca():
    songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
    playcounts = [78, 29, 44, 21, 89, 5]
    plays = {key: value for key, value in zip(songs, playcounts)}
    print(plays)

    plays.update({"Purple Haze": 1})
    plays.update({"Respect": 94})
    print("After:", plays)

    library = {
        "The Best Songs": plays,
        "Sunday Feelings": {}
    }
    print(library)


# Ejecutar todas las funciones
def main():
    mostrar_diccionarios_basicos()
    mostrar_diccionarios_anidados_y_vacios()
    modificar_diccionarios()
    sobrescribir_valores()
    crear_diccionarios_con_zip()
    canciones_y_biblioteca()


if __name__ == "__main__":
    main()
