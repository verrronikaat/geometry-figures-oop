"""
main.py — основная программа лабораторной работы №2.
Вариант 17: Геометрические фигуры.
Сложность: Rare.
"""

from geometry_package import Rectangle, Triangle, Trapezoid
from report_generator import ReportGenerator


def input_float(prompt: str) -> float:
    """Ввод вещественного числа с проверкой."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠ Введите корректное число.")


def create_figure():
    """Меню выбора фигуры и ввод параметров."""
    print("\nВыберите фигуру:")
    print("  1 — Прямоугольник")
    print("  2 — Треугольник")
    print("  3 — Трапеция")

    choice = input("Ваш выбор (1/2/3): ").strip()

    if choice == "1":
        a = input_float("Введите сторону a: ")
        b = input_float("Введите сторону b: ")
        return Rectangle(a, b)

    elif choice == "2":
        a = input_float("Введите сторону a: ")
        b = input_float("Введите сторону b: ")
        c = input_float("Введите сторону c: ")
        return Triangle(a, b, c)

    elif choice == "3":
        a = input_float("Введите основание a: ")
        b = input_float("Введите основание b: ")
        c = input_float("Введите боковую сторону c: ")
        d = input_float("Введите боковую сторону d: ")
        h = input_float("Введите высоту h: ")
        return Trapezoid(a, b, c, d, h)

    else:
        print("⚠ Неверный выбор.")
        return None


def build_summary(figure) -> dict:
    """Формирует словарь с результатами для вывода и отчёта."""
    summary = {
        "Фигура": figure.describe(),
        "Площадь": round(figure.area(), 4),
        "Периметр": round(figure.perimeter(), 4),
    }

    if isinstance(figure, Rectangle):
        summary["Диагональ"] = round(figure.diagonal(), 4)
        summary["R описанной окр."] = round(figure.circumscribed_radius(), 4)

    elif isinstance(figure, Triangle):
        summary["R описанной окр."] = round(figure.circumscribed_radius(), 4)
        summary["r вписанной окр."] = round(figure.inscribed_radius(), 4)

    elif isinstance(figure, Trapezoid):
        summary["Средняя линия"] = round(figure.middle_line(), 4)

    return summary


def main():
    print("=" * 60)
    print("  ЛАБОРАТОРНАЯ РАБОТА №2 — Вариант 17 (Rare)")
    print("  Геометрические фигуры")
    print("=" * 60)

    figure = create_figure()
    if figure is None:
        return

    summary = build_summary(figure)

    print("\n📐 Результаты расчёта:")
    for key, value in summary.items():
        print(f"  {key}: {value}")

    print("\nСохранить отчёт?")
    print("  1 — .docx")
    print("  2 — .xlsx")
    print("  0 — не сохранять")
    save = input("Ваш выбор (1/2/0): ").strip()

    gen = ReportGenerator()
    if save == "1":
        path = gen.save_docx(summary)
        print(f"✅ Отчёт .docx сохранён: {path}")
    elif save == "2":
        path = gen.save_xlsx(summary)
        print(f"✅ Отчёт .xlsx сохранён: {path}")
    else:
        print("ℹ Отчёт не сохранялся.")


if __name__ == "__main__":
    main()