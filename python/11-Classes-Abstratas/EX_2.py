import math
from abc import ABC, abstractmethod

class Figura(ABC):

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

class TrianguloEquilatero(Figura):
    
    def __init__(self, p1, p2, p3):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        self._lateral = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        self._area = math.sqrt(self._lateral ** 2 + (self._lateral/2) ** 2)
        self._perimetro = 3 * self._lateral

    def __repr__(self):
        str = "O triangulo equiláteroformado pelos pontos:\n"
        str += f"{self._p1} {self._p2} {self._p3}\n"
        str += f"tem área de {self.area} cm² e perímetro de {self.perimetro} cm²"
        print(str)

    @property
    def area(self):
        return self._area
    
    @property
    def perimetro(self):
        return self._perimetro

class Quadrado(Figura):
    pass
class Circulo(Figura):
    pass