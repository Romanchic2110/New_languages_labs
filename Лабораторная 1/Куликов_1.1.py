import math

# Узлы интерполяции
x = [0.15, 0.17, 0.18, 0.20]
y = [math.log(xi) for xi in x]
x_star = 0.171


# Метод Лагранжа
def lagrange(x, y, x_star):
    result = 0.0
    for i in range(len(x)):
        term = y[i]
        for j in range(len(x)):
            if i != j:
                term *= (x_star - x[j]) / (x[i] - x[j])
        result += term
    return result


# Таблица разделённых разностей
def divided_differences(x, y):
    table = [y.copy()]
    for k in range(1, len(x)):
        previous = table[-1]
        table.append([
            (previous[i + 1] - previous[i]) / (x[i + k] - x[i])
            for i in range(len(x) - k)
        ])
    return table


# Метод Ньютона
def newton(x, y, x_star):
    table = divided_differences(x, y)
    result = table[0][0]
    product = 1.0
    for k in range(1, len(x)):
        product *= x_star - x[k - 1]
        result += table[k][0] * product
    return result, table


lagrange_result = lagrange(x, y, x_star)
newton_result, table = newton(x, y, x_star)

# Точное значение и фактическая погрешность
exact_value = math.log(x_star)
error_lagrange = abs(exact_value - lagrange_result)
error_newton = abs(exact_value - newton_result)

# Для ln(x): четвёртая производная равна -6/x**4
M4 = 6 / min(x) ** 4
error_estimate = (
        M4 / math.factorial(4)
        * abs((x_star - x[0]) * (x_star - x[1])
              * (x_star - x[2]) * (x_star - x[3]))
)

print("Узлы интерполяции:")
for i in range(len(x)):
    print(f"x{i} = {x[i]:.2f}, y{i} = {y[i]:.10f}")

print("\\nТаблица разделённых разностей:")
for k, row in enumerate(table):
    print(f"Порядок {k}: " + "  ".join(f"{v:.10f}" for v in row))

print(f"\\nИскомая точка: x* = {x_star}")
print(f"Метод Лагранжа: P3(x*) = {lagrange_result:.12f}")
print(f"Метод Ньютона:  P3(x*) = {newton_result:.12f}")
print(f"Точное значение ln(x*): {exact_value:.12f}")
print(f"Фактическая погрешность Лагранжа: {error_lagrange:.12e}")
print(f"Фактическая погрешность Ньютона:  {error_newton:.12e}")
print(f"Теоретическая оценка: |R3| <= {error_estimate:.12e}")
