import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class VectorPlotter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Graficador de Vectores")
        self.geometry("600x500")

        # Etiquetas y campos de entrada
        self.label_x = tk.Label(self, text="Componente x:")
        self.label_x.grid(row=0, column=0, padx=10, pady=10)
        self.entry_x = tk.Entry(self)
        self.entry_x.grid(row=0, column=1, padx=10, pady=10)

        self.label_y = tk.Label(self, text="Componente y:")
        self.label_y.grid(row=1, column=0, padx=10, pady=10)
        self.entry_y = tk.Entry(self)
        self.entry_y.grid(row=1, column=1, padx=10, pady=10)

        # Botón para graficar
        self.plot_button = tk.Button(self, text="Graficar Vector", command=self.plot_vector)
        self.plot_button.grid(row=2, column=0, columnspan=2, pady=20)

        # Área para graficar
        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.grid(row=3, column=0, columnspan=2, pady=20)

    def plot_vector(self):
        try:
            # Obtener las componentes x, y desde las entradas
            x = float(self.entry_x.get())
            y = float(self.entry_y.get())

            # Crear una figura y un gráfico
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='blue')

            # Ajustar los límites del gráfico
            ax.set_xlim(-10, 10)
            ax.set_ylim(-10, 10)
            ax.set_aspect('equal', 'box')
            ax.axhline(0, color='black',linewidth=1)
            ax.axvline(0, color='black',linewidth=1)
            ax.grid(True)

            # Colocar la figura en el canvas de Tkinter
            for widget in self.canvas_frame.winfo_children():
                widget.destroy()

            canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
            canvas.draw()
            canvas.get_tk_widget().pack()

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos para las componentes.")

if __name__ == "__main__":
    app = VectorPlotter()
    app.mainloop()
