import tkinter as tk
from tkinter import messagebox
import math

class Ecuacion():
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def EncontrarRaiz1(self):
        return (-1 * self.B + math.sqrt(self.B ** 2 - 4 * self.A * self.C)) / (2 * self.A)

    def EncontrarRaiz2(self):
        return (-1 * self.B - math.sqrt(self.B ** 2 - 4 * self.A * self.C)) / (2 * self.A)

def CalcularEcuacion():
    nuevaEcuacion = Ecuacion(float(A_entry.get()), float(B_entry.get()), float(C_entry.get()))
    string = f'Raiz 1: {nuevaEcuacion.EncontrarRaiz1()} \nRaiz 2: {nuevaEcuacion.EncontrarRaiz2()}'
    messagebox.showinfo("Resultado", string)

window = tk.Tk()
window.title("Ejercicio 23 Capitulo 4")

A_label = tk.Label(window, text="A:")
A_label.grid(row=0, column=0, sticky="e")
A_entry = tk.Entry(window)
A_entry.grid(row=0, column=1, padx=10, pady=10)

B_label = tk.Label(window, text="B:")
B_label.grid(row=2, column=0, sticky="e")
B_entry = tk.Entry(window)
B_entry.grid(row=2, column=1, padx=10, pady=10)

C_label = tk.Label(window, text="C:")
C_label.grid(row=3, column=0, sticky="e")
C_entry = tk.Entry(window)
C_entry.grid(row=3, column=1, padx=10, pady=10)

# Crear botón para calcular
calcular_button = tk.Button(window, text="Calcular", command=CalcularEcuacion)
calcular_button.grid(row=8, columnspan=2, padx=10, pady=10)

window.mainloop()
