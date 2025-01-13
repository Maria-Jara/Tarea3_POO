import tkinter as tk
from tkinter import messagebox

class Trabajador():
    def __init__(self, Nombre, Horas, Valor):
        self.Nombre = Nombre
        self.Horas = Horas
        self.Valor = Valor

    def getNombre(self):
        return self.Nombre

    def getHoras(self):
        return self.Horas

    def getValor(self):
        return self.Valor

    def calcSalario(self):
        return self.Horas * self.Valor

def verificar():
    trabajador = Trabajador(Nombre=Nombre_entry.get(), Horas=int(Horas_entry.get()), Valor=int(Valor_entry.get()))
    if trabajador.calcSalario() > 450000:
        string = f'Nombre: {trabajador.getNombre()} \nSalario Mensual: {trabajador.calcSalario()}'
    else:
        string = f'Nombre: {trabajador.getNombre()}'
    
    messagebox.showinfo("Resultado", string)

window = tk.Tk()
window.title("Ejercicio 22 Capitulo 4")
window.geometry("400x200")

Nombre_label = tk.Label(window, text="Nombres:")
Nombre_label.grid(row=0, column=0, sticky="e")
Nombre_entry = tk.Entry(window)
Nombre_entry.grid(row=0, column=1, padx=10, pady=10)

Horas_label = tk.Label(window, text="Horas Trabajadas al Mes:")
Horas_label.grid(row=2, column=0, sticky="e")
Horas_entry = tk.Entry(window)
Horas_entry.grid(row=2, column=1, padx=10, pady=10)

Valor_label = tk.Label(window, text="Valor Hora Trabajada:")
Valor_label.grid(row=3, column=0, sticky="e")
Valor_entry = tk.Entry(window)
Valor_entry.grid(row=3, column=1, padx=10, pady=10)

# Crear botón para calcular
calcular_button = tk.Button(window, text="Calcular", command=verificar)
calcular_button.grid(row=8, columnspan=2, padx=10, pady=10)

window.mainloop()
