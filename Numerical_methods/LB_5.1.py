y = [0.10, -0.01, -0.19, -0.11, -0.31, -0.78, -0.64, -0.85, -1.18, -1.39,
     -1.79, -2.02, -2.48, -2.93, -3.26, -3.91, -4.41, -4.91, -5.30, -6.00]

n = len(y)                             
x = [i * 0.1 for i in range(n)] 

def least_squares_poly2(x, y):
    N = len(x)
    Sx   = sum(x)
    Sx2  = sum(xi**2 for xi in x)
    Sx3  = sum(xi**3 for xi in x)
    Sx4  = sum(xi**4 for xi in x)
    Sy   = sum(y)
    Sxy  = sum(x[i] * y[i] for i in range(N))
    Sx2y = sum(x[i]**2 * y[i] for i in range(N))

    A = [[N,   Sx,  Sx2],
         [Sx,  Sx2, Sx3],
         [Sx2, Sx3, Sx4]]
    B = [Sy, Sxy, Sx2y]

    
    def gauss(A, B):
        n = len(A)
        for k in range(n):
            max_row = max(range(k, n), key=lambda i: abs(A[i][k]))
            A[k], A[max_row] = A[max_row], A[k]
            B[k], B[max_row] = B[max_row], B[k]
            for i in range(k+1, n):
                factor = A[i][k] / A[k][k]
                for j in range(k, n):
                    A[i][j] -= factor * A[k][j]
                B[i] -= factor * B[k]
        xs = [0] * n
        for i in range(n-1, -1, -1):
            s = B[i] - sum(A[i][j] * xs[j] for j in range(i+1, n))
            xs[i] = s / A[i][i]
        return xs

    return gauss(A, B)


def P2(xi):
    return a0 + a1*xi + a2*xi**2



a0, a1, a2 = least_squares_poly2(x, y)


print(f"\nКоэффициенты:")
print(f"  a0 = {a0:.6f}")
print(f"  a1 = {a1:.6f}")
print(f"  a2 = {a2:.6f}")
print(f"\nP2(x) = {a0:.6f} + ({a1:.6f})*x + ({a2:.6f})*x^2")


print("\nСравнение исходных и приближённых значений\n")
print(f"{'i':>3} | {'x_i':>6} | {'y_i':>9} | {'P2(x_i)':>10} | "
      f"{'y_i - P2(x_i)':>14} | {'(y_i-P2)^2':>12}")
print("-" * 70)

S = 0
for i in range(n):
    p = P2(x[i])
    d = y[i] - p
    S += d * d
    print(f"{i:>3} | {x[i]:>6.2f} | {y[i]:>9.4f} | {p:>10.6f} | "
          f"{d:>14.6f} | {d*d:>12.6f}")

print("-" * 70)
print(f"Сумма квадратов отклонений: S² = {S:.6f}")

S_sqrt = S ** 0.5

print("\nСреднеквадратичное отклонение\n")
print(f"  S = {S_sqrt:.6f}")
print(f"  S² = {S:.6f}")
