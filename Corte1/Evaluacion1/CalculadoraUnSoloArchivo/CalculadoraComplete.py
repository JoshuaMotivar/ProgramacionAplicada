lass Calculadora:
    def __init__(self):
        self.resultado = 0

    def sumar(self, a, b):
        self.resultado = a + b
        return self.resultado

    def restar(self, a, b):
        self.resultado = a - b
        return self.resultado

    def multiplicar(self, a, b):
        self.resultado = a * b
        return self.resultado

    def dividir(self, a, b):
        if b == 0:
            return "Error: División por cero"
        self.resultado = a / b
        return self.resultado

def main():
    calc = Calculadora()
    
    print("Bienvenido a la Calculadora POO")
    
    while True:
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            operacion = input("Ingrese la operación (+, -, *, /) o 'salir' para terminar: ")
            
            if operacion == '+':
                print("Resultado:", calc.sumar(a, b))
            elif operacion == '-':
                print("Resultado:", calc.restar(a, b))
            elif operacion == '*':
                print("Resultado:", calc.multiplicar(a, b))
            elif operacion == '/':
                print("Resultado:", calc.dividir(a, b))
            elif operacion.lower() == 'salir':
                print("Saliendo de la calculadora.")
                break
            else:
                print("Operación no válida.")
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()