"""
Модуль rectangle.py — класс Rectangle (Прямоугольник).
"""


class Rectangle:
    """Прямоугольник со сторонами a и b."""

    def __init__(self, a: float, b: float):
        if a <= 0 or b <= 0:
            raise ValueError("Стороны прямоугольника должны быть > 0.")
        self.a = float(a)
        self.b = float(b)

    def area(self) -> float:
        """Площадь: S = a * b."""
        return self.a * self.b

    def perimeter(self) -> float:
        """Периметр: P = 2 * (a + b)."""
        return 2 * (self.a + self.b)

    def diagonal(self) -> float:
        """Диагональ: d = sqrt(a^2 + b^2)."""
        return (self.a ** 2 + self.b ** 2) ** 0.5

    def circumscribed_radius(self) -> float:
        """Радиус описанной окружности: R = d / 2."""
        return self.diagonal() / 2

    def describe(self) -> str:
        """Текстовое описание фигуры."""
        return f"Прямоугольник со сторонами a={self.a}, b={self.b}"