import tkinter as tk
from tkinter import messagebox

class Empleado():
    def __init__(self, nombre, codigoEmpleado):
        self.nombre = nombre
        self.codigoEmpleado = codigoEmpleado
        self.HORAS_TRABAJADAS = 0
        self.VALOR_HORA = 0
        self.PORCENTAJE_RETENCION = 0

    # Funciones set
    def setHORAS_TRABAJADAS(self, horas):
        self.HORAS_TRABAJADAS = horas

    def setVALOR_HORA(self, valor):
        self.VALOR_HORA = valor

    def setPORCENTAJE_RETENCION(self, porcentaje):
        self.PORCENTAJE_RETENCION = porcentaje

    # Métodos get
    def getnombres(self):
        return self.nombre

    def getCODIGO(self):
        return self.codigoEmpleado

    def getSALARIO_BRUTO(self):
        return self.VALOR_HORA * self.HORAS_TRABAJADAS

    def getSALARIO_NETO(self):
        return self.getSALARIO_BRUTO() * (1 - (self.PORCENTAJE_RETENCION / 100))

def calculo_salario():
    try:
        nuevo = Empleado(nombre=nombre_entry.get(), codigoEmpleado=codigo_entry.get())
        nuevo.setHORAS_TRABAJADAS(horas=float(horas_entry.get()))
        nuevo.setVALOR_HORA(valor=float(valor_entry.get()))
        nuevo.setPORCENTAJE_RETENCION(porcentaje=float(retencion_entry.get()))

        string = (f'Nombres: {nuevo.getnombres()} \n'
                  f'Codigo: {nuevo.getCODIGO()} \n'
                  f'Salario Neto: {nuevo.getSALARIO_NETO():.2f} \n'
                  f'Salario Bruto: {nuevo.getSALARIO_BRUTO():.2f}')
        messagebox.showinfo("Resultado", string)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos en todos los campos.")

# Ejecutando las configuraciones generales de la ventana ejecutable
window = tk.Tk()
window.title("Ejercicio 18 Capitulo 3")
window.geometry("400x300")

nombre_label = tk.Label(window, text="Nombres:")
nombre_label.grid(row=0, column=0, sticky="e")
nombre_entry = tk.Entry(window)
nombre_entry.grid(row=0, column=1, padx=10, pady=10)

codigo_label = tk.Label(window, text="Codigo:")
codigo_label.grid(row=1, column=0, sticky="e")
codigo_entry = tk.Entry(window)
codigo_entry.grid(row=1, column=1, padx=10, pady=10)

horas_label = tk.Label(window, text="Horas Trabajadas al Mes:")
horas_label.grid(row=2, column=0, sticky="e")
horas_entry = tk.Entry(window)
horas_entry.grid(row=2, column=1, padx=10, pady=10)

valor_label = tk.Label(window, text="Valor Hora Trabajada:")
valor_label.grid(row=3, column=0, sticky="e")
valor_entry = tk.Entry(window)
valor_entry.grid(row=3, column=1, padx=10, pady=10)

retencion_label = tk.Label(window, text="Porcentaje Retención en la Fuente:")
retencion_label.grid(row=4, column=0, sticky="e")
retencion_entry = tk.Entry(window)
retencion_entry.grid(row=4, column=1, padx=10, pady=10)

# Crear botón para calcular el salario
calcular_button = tk.Button(window, text="Calcular", command=calculo_salario)
calcular_button.grid(row=5, columnspan=2, padx=10, pady=10)

window.mainloop()