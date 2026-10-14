"""
main.py — основная программа лабораторной работы №2.
Вариант 17: Геометрические фигуры.
Сложность: Rare.

Графический интерфейс на Tkinter.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from geometry_package import Rectangle, Triangle, Trapezoid
from report_generator import ReportGenerator


class GeometryApp:
    """Графическое приложение для расчёта геометрических фигур."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Лабораторная работа №2 — Вариант 17")
        self.root.geometry("560x680")
        self.root.resizable(False, False)

        self.current_summary = None
        self.report_gen = ReportGenerator()

        self.figure_var = tk.StringVar(value="rectangle")
        self.entries = {}

        self._build_ui()

    # ------------------------------------------------------------------
    def _build_ui(self):
        """Собирает весь интерфейс."""
        # Заголовок
        header = tk.Label(
            self.root,
            text="Геометрические фигуры",
            font=("Arial", 16, "bold"),
            fg="#1f3a93",
        )
        header.pack(pady=(15, 5))

        subtitle = tk.Label(
            self.root,
            text="Вариант 17 — расчёт площади, периметра, радиусов окружностей",
            font=("Arial", 10),
            fg="#555",
        )
        subtitle.pack(pady=(0, 15))

        # ---------- Выбор фигуры ----------
        frame_fig = ttk.LabelFrame(self.root, text="1. Выберите фигуру", padding=10)
        frame_fig.pack(fill="x", padx=15, pady=5)

        for value, text in [
            ("rectangle", "Прямоугольник"),
            ("triangle", "Треугольник"),
            ("trapezoid", "Трапеция"),
        ]:
            rb = ttk.Radiobutton(
                frame_fig,
                text=text,
                value=value,
                variable=self.figure_var,
                command=self._on_figure_change,
            )
            rb.pack(side="left", padx=10)

        # ---------- Параметры ----------
        frame_params = ttk.LabelFrame(self.root, text="2. Введите параметры", padding=10)
        frame_params.pack(fill="x", padx=15, pady=5)

        # Создаём поля для всех параметров (покажем/скроем по необходимости)
        fields = [
            ("a", "Сторона / основание a:"),
            ("b", "Сторона / основание b:"),
            ("c", "Сторона c:"),
            ("d", "Боковая сторона d:"),
            ("h", "Высота h:"),
        ]

        for key, label in fields:
            row = ttk.Frame(frame_params)
            row.pack(fill="x", pady=3)

            lbl = ttk.Label(row, text=label, width=25, anchor="w")
            lbl.pack(side="left")

            entry = ttk.Entry(row, width=20)
            entry.pack(side="left", padx=5)

            self.entries[key] = (row, lbl, entry)

        # ---------- Кнопки ----------
        frame_buttons = ttk.Frame(self.root, padding=10)
        frame_buttons.pack(fill="x", padx=15, pady=5)

        ttk.Button(frame_buttons, text="Рассчитать", command=self._calculate).grid(
            row=0, column=0, padx=5, pady=5, sticky="ew"
        )
        ttk.Button(frame_buttons, text="Очистить", command=self._clear).grid(
            row=0, column=1, padx=5, pady=5, sticky="ew"
        )
        ttk.Button(frame_buttons, text="Сохранить .docx", command=lambda: self._save("docx")).grid(
            row=1, column=0, padx=5, pady=5, sticky="ew"
        )
        ttk.Button(frame_buttons, text="Сохранить .xlsx", command=lambda: self._save("xlsx")).grid(
            row=1, column=1, padx=5, pady=5, sticky="ew"
        )

        frame_buttons.columnconfigure(0, weight=1)
        frame_buttons.columnconfigure(1, weight=1)

        # ---------- Результаты ----------
        frame_result = ttk.LabelFrame(self.root, text="3. Результаты расчёта", padding=10)
        frame_result.pack(fill="both", expand=True, padx=15, pady=5)

        self.result_text = tk.Text(
            frame_result,
            height=12,
            font=("Consolas", 10),
            bg="#f7f7f7",
            fg="#222",
            state="disabled",
            wrap="word",
        )
        self.result_text.pack(fill="both", expand=True)

        # Инициализация: показываем поля для прямоугольника
        self._on_figure_change()

    # ------------------------------------------------------------------
    def _on_figure_change(self):
        """Показывает/скрывает поля в зависимости от выбранной фигуры."""
        figure = self.figure_var.get()

        # По умолчанию показываем все
        visible = {"a", "b", "c", "d", "h"}

        if figure == "rectangle":
            visible = {"a", "b"}
        elif figure == "triangle":
            visible = {"a", "b", "c"}
        elif figure == "trapezoid":
            visible = {"a", "b", "c", "d", "h"}

        for key, (row, lbl, entry) in self.entries.items():
            if key in visible:
                row.pack(fill="x", pady=3)
            else:
                row.pack_forget()

    # ------------------------------------------------------------------
    def _get_float(self, key: str) -> float:
        """Возвращает введённое число или None при ошибке."""
        entry = self.entries[key][2]
        value = entry.get().strip()
        if not value:
            return None
        try:
            return float(value)
        except ValueError:
            return None

    # ------------------------------------------------------------------
    def _calculate(self):
        """Обработчик кнопки «Рассчитать»."""
        figure_type = self.figure_var.get()

        try:
            if figure_type == "rectangle":
                a = self._get_float("a")
                b = self._get_float("b")
                if a is None or b is None:
                    raise ValueError("Введите обе стороны a и b.")
                figure = Rectangle(a, b)

            elif figure_type == "triangle":
                a = self._get_float("a")
                b = self._get_float("b")
                c = self._get_float("c")
                if a is None or b is None or c is None:
                    raise ValueError("Введите все три стороны a, b, c.")
                figure = Triangle(a, b, c)

            elif figure_type == "trapezoid":
                a = self._get_float("a")
                b = self._get_float("b")
                c = self._get_float("c")
                d = self._get_float("d")
                h = self._get_float("h")
                if None in (a, b, c, d, h):
                    raise ValueError("Введите все параметры трапеции: a, b, c, d, h.")
                figure = Trapezoid(a, b, c, d, h)

            else:
                raise ValueError("Выберите фигуру.")

        except ValueError as e:
            messagebox.showerror("Ошибка ввода", str(e))
            return

        # Собираем summary
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

        self.current_summary = summary
        self._show_results(summary)

    # ------------------------------------------------------------------
    def _show_results(self, summary: dict):
        """Отображает результаты в текстовом поле."""
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", "end")

        for key, value in summary.items():
            self.result_text.insert("end", f"{key}: {value}\n")

        self.result_text.config(state="disabled")

    # ------------------------------------------------------------------
    def _clear(self):
        """Очищает все поля и результаты."""
        for _, _, entry in self.entries.values():
            entry.delete(0, "end")
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", "end")
        self.result_text.config(state="disabled")
        self.current_summary = None

    # ------------------------------------------------------------------
    def _save(self, fmt: str):
        """Сохраняет отчёт в .docx или .xlsx."""
        if self.current_summary is None:
            messagebox.showwarning("Нет данных", "Сначала выполните расчёт.")
            return

        try:
            if fmt == "docx":
                path = self.report_gen.save_docx(self.current_summary)
            else:
                path = self.report_gen.save_xlsx(self.current_summary)

            messagebox.showinfo("Готово", f"Отчёт сохранён:\n{path}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить: {e}")


def main():
    root = tk.Tk()
    app = GeometryApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()