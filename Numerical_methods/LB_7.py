import math
from tabulate import tabulate

def integrate_and_estimate(f, a, b, n, title):
    print("\n" + "=" * 80)
    print(f" ИНТЕГРАЛ {title}")
    print("=" * 80)

    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]

    sum_rect = sum(f((x[i] + x[i+1]) / 2) for i in range(n))
    I_rect = h * sum_rect

    I_trap = h * (y[0] + y[-1] + 2 * sum(y[1:-1])) / 2

    sum_odd = sum(y[1::2])
    sum_even = sum(y[2:-1:2])
    I_simp = (h / 3) * (y[0] + y[-1] + 4 * sum_odd + 2 * sum_even)

    print(f"Шаг h = {h:.2f}\n")
    
    results_table = [
        ["Прямоугольники (средние)", f"{I_rect:.6f}"],
        ["Трапеции", f"{I_trap:.6f}"],
        ["Симпсон", f"{I_simp:.6f}"]
    ]
    print(tabulate(results_table, headers=["Метод", "Значение интеграла"], tablefmt="grid"))

    diffs = [y[:]]
    for order in range(1, 5):
        prev = diffs[-1]
        curr = [prev[i+1] - prev[i] for i in range(len(prev) - 1)]
        diffs.append(curr)

    table_data = []
    for i in range(n + 1):
        row = [i, f"{x[i]:.3f}", f"{y[i]:.5f}"]
        for order in range(1, 5):
            if i < len(diffs[order]):
                row.append(f"{diffs[order][i] * 10000:.2f}")
            else:
                row.append("")
        table_data.append(row)

    print("\nТаблица конечных разностей (значения увеличены на 10^4 для наглядности):")
    headers = ["i", "x_i", "y_i", "Δy", "Δ²y", "Δ³y", "Δ⁴y"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

    max_d2 = max(abs(d) for d in diffs[2])
    max_d4 = max(abs(d) for d in diffs[4])

    R_rect = (b - a) / 24 * max_d2
    R_trap = (b - a) / 12 * max_d2
    R_simp = (b - a) / 180 * max_d4

    error_table = [
        ["Макс. |Δ²y|", f"{max_d2:.6e}"],
        ["Макс. |Δ⁴y|", f"{max_d4:.6e}"],
        ["R (прямоугольники)", f"≤ {R_rect:.6e}"],
        ["R (трапеции)", f"≤ {R_trap:.6e}"],
        ["R (Симпсон)", f"≤ {R_simp:.6e}"]
    ]
    
    print("\nОЦЕНКА ПОГРЕШНОСТИ:")
    print(tabulate(error_table, headers=["Параметр", "Значение"], tablefmt="grid"))
    print("\n")

def f_a(x):
    return 1 / math.sqrt(0.5 * x**2 + 1)

def f_b(x):
    return math.tan(x**2) / (x + 1)

integrate_and_estimate(f_a, 3.2, 4.0, 10, "а)  ∫ dx / √(0.5x² + 1)  [3.2, 4.0]")
integrate_and_estimate(f_b, 0.5, 1.2, 10, "б)  ∫ tg(x²)/(x+1) dx  [0.5, 1.2]")