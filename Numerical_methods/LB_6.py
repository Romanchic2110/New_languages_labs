import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.85, 0.90, 0.95, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30])
y = np.array([0.75128, 0.78333, 0.81342, 0.84147, 0.86742, 0.89121, 0.91276, 0.93204, 0.94898, 0.96356])
n = len(x)
h = x[1] - x[0]

dy = np.zeros(n)
d2y = np.zeros(n)

for i in range(n):
    if i == 0:
        dy[i] = (-3*y[i] + 4*y[i+1] - y[i+2]) / (2*h)
        d2y[i] = (2*y[i] - 5*y[i+1] + 4*y[i+2] - y[i+3]) / (h**2)
    elif i == n - 1:
        dy[i] = (3*y[i] - 4*y[i-1] + y[i-2]) / (2*h)
        d2y[i] = (2*y[i] - 5*y[i-1] + 4*y[i-2] - y[i-3]) / (h**2)
    else:
        dy[i] = (y[i+1] - y[i-1]) / (2*h)
        d2y[i] = (y[i-1] - 2*y[i] + y[i+1]) / (h**2)

p_coeffs = np.polyfit(x, y, n - 1)
p = np.poly1d(p_coeffs)

dp = np.polyder(p, 1)
d2p = np.polyder(p, 2)

dy_analytical = dp(x)
d2y_analytical = d2p(x)

x_dense = np.linspace(min(x)-0.02, max(x)+0.02, 500)

print("=" * 80)
print(f"{'x':>6} | {'y=f(x)':>10} | {'dy (числ.)':>12} | {'dy (аналит.)':>14} | {'d2y (числ.)':>12} | {'d2y (аналит.)':>14}")
print("-" * 80)
for i in range(n):
    print(f"{x[i]:>6.2f} | {y[i]:>10.5f} | {dy[i]:>12.5f} | {dy_analytical[i]:>14.5f} | {d2y[i]:>12.5f} | {d2y_analytical[i]:>14.5f}")
print("=" * 80)

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(x_dense, p(x_dense), 'g-', label='Многочлен 9-й степени', alpha=0.6)
plt.plot(x, y, 'ro', label='Исходные точки')
plt.title('Задание 1: Интерполяция функции')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x_dense, dp(x_dense), 'b-', label="Производная многочлена", alpha=0.6)
plt.plot(x, dy, 'rs', markersize=8, label="Численная производная")
plt.title('Сравнение первой производной')
plt.xlabel('x')
plt.ylabel("y'")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(x_dense, d2p(x_dense), 'm-', label="Вторая производная многочлена", alpha=0.6)
plt.plot(x, d2y, 'r^', markersize=8, label="Численная вторая производная")
plt.title('Сравнение второй производной')
plt.xlabel('x')
plt.ylabel("y''")
plt.legend()
plt.grid(True)
plt.show()