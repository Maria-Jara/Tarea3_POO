import tkinter as tk
from tkinter import messagebox
import math

class TRIANGULO():
    def __init__(self, LADO):
        self.LADO = LADO

    def getP(self):
        return self.LADO * 3

    def getH(self):
        return math.sqrt(self.LADO ** 2 - (self.LADO / 2) ** 2)

    def getA(self):
        return math.sqrt(3) * (1 / 4) * self.LADO ** 2

def calculoMedidas():
    TRI = TRIANGULO(float(lado_entry.get()))
    string = f'Perimetro: {TRI.getP()} \nAltura: {TRI.getH()} \nArea: {TRI.getA()} \n'
    messagebox.showinfo("Resultado", string)

window = tk.Tk()
window.title("Ejercicio 19 Capitulo 3")

lado_label = tk.Label(window, text="Lado:")
lado_label.grid(row=0, column=0)

lado_entry = tk.Entry(window)
lado_entry.grid(row=0, column=1, padx=10, pady=10)

# Crear botón para calcular
calcular_button = tk.Button(window, text="Calcular", command=calculoMedidas)
calcular_button.grid(row=8, columnspan=2, padx=10, pady=10)

window.mainloop()
