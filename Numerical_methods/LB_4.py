import math

x = [0.20, 0.40, 0.45, 0.60, 0.70, 0.75]
y = [math.exp(i) for i in x]  

z_points = [0.250, 0.442, 0.730]


def build_cubic_spline(x, y):

    n = len(x) - 1  
    h = [x[i+1] - x[i] for i in range(n)]

    m = n - 1                       
    A = [0] * m   
    B = [0] * m   
    C = [0] * m   
    F = [0] * m   

    for k in range(m):
        i = k + 1                    
        A[k] = h[i-1]
        B[k] = 2 * (h[i-1] + h[i])
        C[k] = h[i]
        F[k] = 3.0 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1])

    alpha = [0] * m
    beta  = [0] * m
    alpha[0] = -C[0] / B[0]
    beta[0]  =  F[0] / B[0]

    for k in range(1, m):
        denom = B[k] + A[k] * alpha[k-1]
        alpha[k] = -C[k] / denom
        beta[k]  = (F[k] - A[k] * beta[k-1]) / denom

    c_inner = [0] * m
    c_inner[m-1] = beta[m-1]
    for k in range(m-2, -1, -1):
        c_inner[k] = alpha[k] * c_inner[k+1] + beta[k]

    c = [0] * (n + 1)
    for k in range(m):
        c[k+1] = c_inner[k]

    d = [0] * n
    for i in range(n):
        if i == 0:
            d[i] = c[1] / (3.0 * h[0])
        else:
            d[i] = (c[i+1] - c[i]) / (3.0 * h[i])

    b = [0] * n
    for i in range(n):
        b[i] = (y[i+1] - y[i]) / h[i] - h[i] * c[i+1] - h[i]**2 * d[i]

    a = y[:n]
    return a, b, c[:n], d


def spline_value(x, a, b, c, d, t):
    n = len(a)
    i = 0
    for k in range(n):
        if x[k] <= t <= x[k+1]:
            i = k
            break
    dx = t - x[i]
    return a[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3



a, b, c, d = build_cubic_spline(x, y)


print(f"\nУзлы x: {x}")
print(f"Значения e^x: {[round(v, 6) for v in y]}")

print("\n\nКоэффициенты сплайна на каждом отрезке:\n")
for i in range(len(a)):
    print(f"  [{x[i]}, {x[i+1]}]: a={a[i]:.6f}, b={b[i]:.6f}, "
          f"c={c[i]:.6f}, d={d[i]:.6f}")


print("\n\nЗначения сплайна в точках z:\n")
for z in z_points:
    val = spline_value(x, a, b, c, d, z)
    exact = math.exp(z)
    err = abs(val - exact)
    print(f"  S({z}) = {val:.6f}   e^{z} = {exact:.6f}   |Δ| = {err:.2e}")

