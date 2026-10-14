"""
Модуль trapezoid.py — класс Trapezoid (Трапеция).
"""


class Trapezoid:
    """Трапеция с основаниями a, b, боковыми сторонами c, d и высотой h."""

    def __init__(self, a: float, b: float, c: float, d: float, h: float):
        if a <= 0 or b <= 0 or c <= 0 or d <= 0 or h <= 0:
            raise ValueError("Все параметры трапеции должны быть > 0.")
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)
        self.h = float(h)

    def area(self) -> float:
        """Площадь: S = (a + b) / 2 * h."""
        return (self.a + self.b) / 2 * self.h

    def perimeter(self) -> float:
        """Периметр: P = a + b + c + d."""
        return self.a + self.b + self.c + self.d

    def middle_line(self) -> float:
        """Средняя линия: m = (a + b) / 2."""
        return (self.a + self.b) / 2

    def describe(self) -> str:
        """Текстовое описание фигуры."""
        return (f"Трапеция: основания a={self.a}, b={self.b}, "
                f"боковые c={self.c}, d={self.d}, высота h={self.h}")