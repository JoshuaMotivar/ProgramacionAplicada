class Calculadora:
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