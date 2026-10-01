import math

x_nodes = [3.60, 3.65, 3.70]
y_nodes = [35.598, 38.475, 40.447]


x_res = 3.62


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


def error_estimate(x_nodes, x_res, true_value):
    n = len(x_nodes) - 1 
    M_n1 = math.exp(x_nodes[-1]) 
    
    omega = 1
    for i in x_nodes:
        omega *= (x_res - i)
    
    error_bound = abs(M_n1 / math.factorial(n + 1) * omega)
    
    actual_error = abs(true_value - lagrange_interpolation(x_nodes, y_nodes, x_res))
    
    return error_bound, actual_error


lagrange_val = lagrange_interpolation(x_nodes, y_nodes, x_res)

newton_val = newton_interpolation(x_nodes, y_nodes, x_res)

true_val = math.exp(x_res)

error_bound, actual_error = error_estimate(x_nodes, x_res, true_val)

print(f"\nЗначение по Лагранжу: {lagrange_val:.6f}")
print(f"Значение по Ньютону:  {newton_val:.6f}")
print(f"Истинное значение:    {true_val:.6f}")
print(f"Оценка погрешности:   {error_bound:.6f}")
print(f"Фактическая погрешность: {actual_error:.6f}")
