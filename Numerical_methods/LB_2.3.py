import math

x_nodes = [0.16, 0.18, 0.19, 0.22]
y_nodes = [math.cos(x) for x in x_nodes] 
x_res = 0.165


def lagrange_interpolation(x_nodes, y_nodes, x):
    n = len(x_nodes)
    res = 0
    
    for i in range(n):
        t = y_nodes[i]
        for j in range(n):
            if i != j:
                t *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        res += t
        
    return res


def newton_divided_differences(x_nodes, y_nodes):

    n = len(x_nodes)
    div_diff = [[0] * n for _ in range(n)]
    
    for i in range(n):
        div_diff[i][0] = y_nodes[i]
        
    for j in range(1, n):
        for i in range(n - j):
            div_diff[i][j] = (div_diff[i+1][j-1] - div_diff[i][j-1]) / (x_nodes[i+j] - x_nodes[i])
    
    return div_diff


def newton_interpolation(x_nodes, y_nodes, x):

    n = len(x_nodes)
    div_diff = newton_divided_differences(x_nodes, y_nodes)
    
    res = div_diff[0][0]
    product = 1
    
    for i in range(1, n):
        product *= (x - x_nodes[i-1])
        res += div_diff[0][i] * product
        
    return res



def error_estimate(x_nodes, x_res):
    n = len(x_nodes) - 1 
    M_n1 = 1 
    
    omega = 1
    for i in x_nodes:
        omega *= (x_res - i)

    return abs(M_n1 / math.factorial(n + 1) * omega)


lagrange_val = lagrange_interpolation(x_nodes, y_nodes, x_res)
newton_val = newton_interpolation(x_nodes, y_nodes, x_res)
true_val = math.cos(x_res)
error_bound = error_estimate(x_nodes, x_res)
actual_error = abs(true_val - lagrange_val)

print(f"\nВариант 12: f(x) = cos(x), x* = {x_res}")
print(f"Узлы: {x_nodes}")
print(f"\nЗначения cos: {[round(y, 6) for y in y_nodes]}")
print(f"Значение по Лагранжу:     {lagrange_val}")
print(f"Значение по Ньютону:      {newton_val}")
print(f"Истинное значение cos:    {true_val}")
print(f"\nОценка погрешности:       {error_bound}")
print(f"Фактическая погрешность:  {actual_error}")
