import math

t_data = [14.5, 30.0, 64.5, 74.5, 86.7, 94.5, 98.9]
k_data = [0.000, 0.004, 0.018, 0.029, 0.051, 0.073, 0.090]


pairs = [(t, k) for t, k in zip(t_data, k_data) if k > 0]
t = [p[0] for p in pairs]
k = [p[1] for p in pairs]
N = len(t)

Y = [math.log(ki) for ki in k]

St  = sum(t)
St2 = sum(ti * ti for ti in t)
SY  = sum(Y)
StY = sum(t[i] * Y[i] for i in range(N))

det = N * St2 - St * St
B = (SY * St2 - StY * St) / det
A = (N * StY - St * SY) / det

a = A
b = math.exp(B)

print("Исходные данные:")
print(f"  t = {t_data}")
print(f"  k = {k_data}")

print("\nРезультат:")
print(f"  a = {a:.10f}")
print(f"  b = {b:.10f}")
print(f"  k(t) = {b:.8f} * exp({a:.8f} * t)")

print("\nСравнение:")
print(f"{'t':>7} | {'k':>9} | {'k(t)':>12} | {'k - k(t)':>14}")
print("-" * 52)
for i in range(N):
    km = b * math.exp(a * t[i])
    print(f"{t[i]:>7.2f} | {k[i]:>9.3f} | {km:>12.8f} | {k[i] - km:>14.8f}")