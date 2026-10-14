"""
Модуль triangle.py — класс Triangle (Треугольник).
"""

import math


class Triangle:
    """Треугольник со сторонами a, b, c."""

    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны треугольника должны быть > 0.")
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Треугольник с такими сторонами не существует.")
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def perimeter(self) -> float:
        """Периметр: P = a + b + c."""
        return self.a + self.b + self.c

    def area(self) -> float:
        """Площадь по формуле Герона."""
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def circumscribed_radius(self) -> float:
        """Радиус описанной окружности: R = abc / (4S)."""
        S = self.area()
        return (self.a * self.b * self.c) / (4 * S)

    def inscribed_radius(self) -> float:
        """Радиус вписанной окружности: r = S / p."""
        S = self.area()
        p = self.perimeter() / 2
        return S / p

    def describe(self) -> str:
        """Текстовое описание фигуры."""
        return f"Треугольник со сторонами a={self.a}, b={self.b}, c={self.c}"