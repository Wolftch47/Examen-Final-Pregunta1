from geometria import Geometria
import math

class Triangulo(Geometria):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def dibujar(self, canvas):
        # Coordenadas del triángulo
        x0, y0 = 100, 200
        x1, y1 = x0 + self.base, y0
        x2, y2 = x0 + (self.base / 2), y0 - self.altura

        # Dibujar el triángulo en canva
        canvas.create_polygon(x0, y0, x1, y1, x2, y2, outline="black", fill="lightblue", width=2)

        # Calcular y mostrar el área y perímetro
        area = self.calcular_area()
        perimetro = self.calcular_perimetro()
        canvas.create_text(200, 220, text=f"Área: {area:.2f}")
        canvas.create_text(200, 240, text=f"Perímetro: {perimetro:.2f}")
