import tkinter as tk
from triangulo import Triangulo

# Crear instancia de la clase Triangulo
triangulo = Triangulo(base=200, altura=150, lado1=200, lado2=80, lado3=60)

# Crear ventana principal
root = tk.Tk()
root.title("Triángulo - Área y Perímetro")

# Crear un canvas para dibujar
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Dibujar el triángulo y mostrar datos
triangulo.dibujar(canvas)

# Ejecutar ventana
root.mainloop()
