import tkinter as tk
from tkinter import messagebox

# Clase que representa la lógica de la calculadora
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b

# Clase para la interfaz gráfica
class CalculadoraGUI:
    def __init__(self, root):
        self.calc = Calculadora()
        self.root = root
        self.root.title("Calculadora POO")

        # Entradas
        self.entrada1 = tk.Entry(root, width=15)
        self.entrada1.grid(row=0, column=0, padx=10, pady=10)

        self.entrada2 = tk.Entry(root, width=15)
        self.entrada2.grid(row=0, column=1, padx=10, pady=10)

        # Botones
        tk.Button(root, text="+", width=5, command=self.sumar).grid(row=1, column=0)
        tk.Button(root, text="-", width=5, command=self.restar).grid(row=1, column=1)
        tk.Button(root, text="×", width=5, command=self.multiplicar).grid(row=2, column=0)
        tk.Button(root, text="÷", width=5, command=self.dividir).grid(row=2, column=1)

        # Resultado
        self.resultado = tk.Label(root, text="Resultado: ", font=("Arial", 14))
        self.resultado.grid(row=3, column=0, columnspan=2, pady=10)

    def obtener_valores(self):
        try:
            a = float(self.entrada1.get())
            b = float(self.entrada2.get())
            return a, b
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa números válidos")
            return None, None

    def sumar(self):
        a, b = self.obtener_valores()
        if a is not None:
            res = self.calc.sumar(a, b)
            self.resultado.config(text=f"Resultado: {res}")

    def restar(self):
        a, b = self.obtener_valores()
        if a is not None:
            res = self.calc.restar(a, b)
            self.resultado.config(text=f"Resultado: {res}")

    def multiplicar(self):
        a, b = self.obtener_valores()
        if a is not None:
            res = self.calc.multiplicar(a, b)
            self.resultado.config(text=f"Resultado: {res}")

    def dividir(self):
        a, b = self.obtener_valores()
        if a is not None:
            try:
                res = self.calc.dividir(a, b)
                self.resultado.config(text=f"Resultado: {res}")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

# Crear la ventana principal y ejecutar
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()
