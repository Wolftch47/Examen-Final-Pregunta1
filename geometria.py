from abc import ABC, abstractmethod

class Geometria(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

    @abstractmethod
    def dibujar(self, canvas):
        pass
