# Sección 1: Obtener un valor por su clave
def obtener_valores():
    building_heights = {
        "Burj Khalifa": 828,
        "Shanghai Tower": 632,
        "Abraj Al Bait": 601,
        "Ping An": 599,
        "Lotte World Tower": 554.5,
        "One World Trade": 541.3
    }
    print(building_heights["Burj Khalifa"])
    print(building_heights["Ping An"])

    zodiac_elements = {
        "water": ["Cancer", "Scorpio", "Pisces"],
        "fire": ["Aries", "Leo", "Sagittarius"],
        "earth": ["Taurus", "Virgo", "Capricorn"],
        "air": ["Gemini", "Libra", "Aquarius"]
    }
    print(zodiac_elements["earth"])
    print(zodiac_elements["fire"])

# Sección 2: Comprobación de clave existente y get()
def obtener_con_comprobacion():
    building_heights = {
        "Burj Khalifa": 828,
        "Shanghai Tower": 632,
        "Abraj Al Bait": 601,
        "Ping An": 599,
        "Lotte World Tower": 554.5,
        "One World Trade": 541.3
    }
    key_to_check = "Landmark 81"
    if key_to_check in building_heights:
        print(building_heights[key_to_check])

    zodiac_elements = {
        "water": ["Cancer", "Scorpio", "Pisces"],
        "fire": ["Aries", "Leo", "Sagittarius"],
        "earth": ["Taurus", "Virgo", "Capricorn"],
        "air": ["Gemini", "Libra", "Aquarius"]
    }
    zodiac_elements["energy"] = "Not a Zodiac element"
    if "energy" in zodiac_elements:
        print(zodiac_elements["energy"])

    print(building_heights.get("Shanghai Tower"))  # Devuelve 632
    print(building_heights.get("My House"))        # Devuelve None

# Sección 3: Get seguro y condiciones
def uso_get_seguro():
    user_ids = {
        "teraCoder": 100019,
        "pythonGuy": 182921,
        "samTheJavaMaam": 123112,
        "lyleLoop": 102931,
        "keysmithKeith": 129384
    }
    tc_id = user_ids.get("teraCoder", 1000)
    print(tc_id)

    stack_id = user_ids.get("superStackSmash", 100000)
    print(stack_id)

# Sección 4: Eliminar claves con pop()
def eliminar_claves():
    raffle = {
        223842: "Teddy Bear",
        872921: "Concert Tickets",
        320291: "Gift Basket",
        412123: "Necklace",
        298787: "Pasta Maker"
    }
    print(raffle.pop(320291, "No Prize"))
    print(raffle)
    print(raffle.pop(100000, "No Prize"))
    print(raffle)
    print(raffle.pop(872921, "Concert Tickets"))
    print(raffle)

    available_items = {
        "health potion": 10,
        "cake of the cure": 5,
        "green elixir": 20,
        "strength sandwich": 25,
        "stamina grains": 15,
        "power stew": 30
    }
    health_points = 20
    health_points += available_items.pop("stamina grains", 0)
    health_points += available_items.pop("power stew", 0)
    health_points += available_items.pop("mystic bread", 0)
    print(available_items)
    print(health_points)

# Sección 5: Obtener claves y valores
def claves_y_valores():
    test_scores = {
        "Grace": [80, 72, 90],
        "Jeffrey": [88, 68, 81],
        "Sylvia": [80, 82, 84],
        "Pedro": [98, 96, 95],
        "Martin": [78, 80, 78],
        "Dina": [64, 60, 75]
    }
    print(list(test_scores))
    for student in test_scores.keys():
        print(student)

    user_ids = {
        "teraCoder": 100019,
        "pythonGuy": 182921,
        "samTheJavaMaam": 123112,
        "lyleLoop": 102931,
        "keysmithKeith": 129384
    }
    num_exercises = {
        "functions": 10,
        "syntax": 13,
        "control flow": 15,
        "loops": 22,
        "lists": 19,
        "classes": 18,
        "dictionaries": 18
    }
    print(user_ids.keys())
    print(num_exercises.keys())

    for score_list in test_scores.values():
        print(score_list)

    total_exercises = sum(num_exercises.values())
    print(total_exercises)

# Sección 6: Obtener todos los elementos (clave y valor)
def mostrar_items():
    biggest_brands = {
        "Apple": 184,
        "Google": 141.7,
        "Microsoft": 80,
        "Coca-Cola": 69.7,
        "Amazon": 64.8
    }
    for company, value in biggest_brands.items():
        print(company + " has a value of " + str(value) + " billion dollars.")

    pct_women_in_occupation = {
        "CEO": 28,
        "Engineering Manager": 9,
        "Pharmacist": 58,
        "Physician": 40,
        "Lawyer": 37,
        "Aerospace Engineer": 9
    }
    for occupation, percentage in pct_women_in_occupation.items():
        print("Women make up " + str(percentage) + " percent of " + occupation + "s.")

# Ejecutar todas las funciones
def main():
    obtener_valores()
    obtener_con_comprobacion()
    uso_get_seguro()
    eliminar_claves()
    claves_y_valores()
    mostrar_items()

if __name__ == "__main__":
    main()
