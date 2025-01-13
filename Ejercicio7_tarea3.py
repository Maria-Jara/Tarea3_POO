import tkinter as tk
from tkinter import messagebox

class Comparacion():
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def comparar(self):
        if self.A > self.B:
            return 1
        else:
            if self.A == self.B:
                return 2
            else:
                return 3

def calcular():
    NuevaComparacion = Comparacion(float(A_entry.get()), float(B_entry.get()))
    Resultado = NuevaComparacion.comparar()
    if Resultado == 1:
        string = f'{float(A_entry.get())} es mayor que {float(B_entry.get())}'
    elif Resultado == 2:
        string = f'{float(A_entry.get())} es igual a {float(B_entry.get())}'
    else:
        string = f'{float(A_entry.get())} es menor que {float(B_entry.get())}'
    
    messagebox.showinfo("Resultado", string)

window = tk.Tk()
window.title("Ejercicio 7 Capitulo 4")

A_label = tk.Label(window, text="Numero A:")
A_label.grid(row=0, column=0)

A_entry = tk.Entry(window)
A_entry.grid(row=0, column=1, padx=10, pady=10)

B_label = tk.Label(window, text="Numero B:")
B_label.grid(row=1, column=0)

B_entry = tk.Entry(window)
B_entry.grid(row=1, column=1, padx=10, pady=10)

# Crear botón para calcular
calcular_button = tk.Button(window, text="Calcular", command=calcular)
calcular_button.grid(row=8, columnspan=2, padx=10, pady=10)

window.mainloop()
