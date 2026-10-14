"""
Пакет geometry_package.

Содержит 3 модуля с классами геометрических фигур:
- rectangle: класс Rectangle (Прямоугольник)
- triangle:  класс Triangle (Треугольник)
- trapezoid: класс Trapezoid (Трапеция)
"""

from .rectangle import Rectangle
from .triangle import Triangle
from .trapezoid import Trapezoid

__all__ = ["Rectangle", "Triangle", "Trapezoid"]
__version__ = "1.0.0"