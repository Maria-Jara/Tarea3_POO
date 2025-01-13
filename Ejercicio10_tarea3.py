import tkinter as tk
from tkinter import messagebox

class Estudiante():
    def __init__(self, NUMERO, NOMBRE):
        self.NUMEROIns = NUMERO
        self.NOMBRE = NOMBRE

    def getNUMERO(self):
        return self.NUMEROIns

    def getNOMBRE(self):
        return self.NOMBRE

    def setPATRIMONIO(self, valor):
        self.PATRIMONIO = valor

    def setEstrato(self, estrato):
        self.estrato = estrato

    def getMATRICULA(self):
        if self.PATRIMONIO > 2000000 and self.estrato > 3:
            return 50000 + (self.PATRIMONIO * 0.03)
        return 50000

def calcular_matricula():
    estudiante = Estudiante(NUMERO=numero_inscripcion_entry.get(), NOMBRE=nombre_entry.get())
    estudiante.setEstrato(estrato=int(estrato_entry.get()))
    estudiante.setPATRIMONIO(valor=float(patrimonio_entry.get()))
    valor = estudiante.getMATRICULA()
    string = f'Numero Inscripcion: {estudiante.getNUMERO()} \nNombres: {estudiante.getNOMBRE()} \nMatricula: {valor}'
    messagebox.showinfo("Resultado", string)

window = tk.Tk()
window.title("Ejercicio 10 Capitulo 4")
window.geometry("400x250")

NUMERO_inscripcion_label = tk.Label(window, text="Numero Inscripcion:")
NUMERO_inscripcion_label.grid(row=0, column=0, sticky="e")
numero_inscripcion_entry = tk.Entry(window)
numero_inscripcion_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

NOMBRE_label = tk.Label(window, text="Nombres:")
NOMBRE_label.grid(row=1, column=0, sticky="e")
nombre_entry = tk.Entry(window)
nombre_entry.grid(row=1, column=1, padx=10, pady=10)

PATRIMONIO_label = tk.Label(window, text="Patrimonio:")
PATRIMONIO_label.grid(row=2, column=0, sticky="e")
patrimonio_entry = tk.Entry(window)
patrimonio_entry.grid(row=2, column=1, padx=10, pady=10, sticky="e")

estrato_label = tk.Label(window, text="Estrato:")
estrato_label.grid(row=3, column=0, sticky="e")
estrato_entry = tk.Entry(window)
estrato_entry.grid(row=3, column=1, padx=10, pady=10, sticky="e")

calcular_button = tk.Button(window, text="Calcular", command=calcular_matricula)
calcular_button.grid(row=8, columnspan=2, padx=10, pady=10)

window.mainloop()
