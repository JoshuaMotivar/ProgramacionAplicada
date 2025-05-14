from cuenta import CuentaBancaria
from menu import mostrar_menu

def ejecutar_cajero():
    nombre = input("🧑‍💼 Ingresa el nombre del titular: ")
    cuenta = CuentaBancaria(nombre, 5000000) 

    while True:
        mostrar_menu()
        try:
            opcion = int(input("👉 Elige una opción (1-4): "))

            if opcion == 1:
                cuenta.ver_saldo()

            elif opcion == 2:
                monto = float(input("💵 Ingrese el monto a depositar (COP): "))
                cuenta.depositar(monto)

            elif opcion == 3:
                monto = float(input("🏧 Ingrese el monto a retirar (COP): "))
                cuenta.retirar(monto)

            elif opcion == 4:
                print(f"\n👋 Gracias, {nombre}, por usar el cajero. ¡Hasta pronto!")
                break

            else:
                print("\n⚠️ Opción no válida. Intenta nuevamente.")
        
        except ValueError:
            print("\n❌ Entrada no válida. Por favor ingresa números.")


if __name__ == "__main__":
    ejecutar_cajero()