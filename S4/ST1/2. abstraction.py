"""
Abstractizarea este similara cu mostenirea, cu cateva diferente:
- clasa de baza (parinte) este o clasa abstracta, adica NU poate crea obiecte (nu avem metoda de init)
- clasa de baza are doar metode abstracte, adica metode goale, care aarunca o exceptie (NotImplementedError) daca sunt apelate
- astfel, clasa de baza actioneaza ca un sablon de functionalitati pentru clasele copii (adica toate
    clasele copil TREBUIE sa implementeze metodele definite in clasa de baza).
- clasa de baza TREBUIE sa mosteneasca clasa ABC din pachetul abc (python standard)
- toate metodele clasei de baza trebuie anotate cu @abstractmethod
"""

from abc import ABC, abstractmethod
from math import pi

class FormaGeometrica(ABC):

    @abstractmethod
    def compute_area(self):
        raise NotImplementedError

    @abstractmethod
    def compute_perimeter(self):
        raise NotImplementedError


class Circle(FormaGeometrica):
    def __init__(self, r, color):  #r - raza cercului
        self.r = r
        self.color = color

    def compute_area(self): # Aria cercului
        return int(pi * (self.r * self.r))

    def compute_perimeter(self):
        return int(pi * 2 * self.r)


class Rectangle(FormaGeometrica):
    def __init__(self, l, L, color='Blue'):
        self.l = l
        self.L = L
        self.color = color

    def compute_area(self):
        return self.l*self.L

    def compute_perimeter(self):
        return 2*self.l+2*self.L


c = Circle(5, 'red')
r = Rectangle(4, 10)