
x_nodes = [10, 15, 17, 20]
y_nodes = [3, 7, 11, 17]
y_res = 10


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


def bisection_method(func, a, b, tol=1e-10, max_iter=1000):
    f_a = func(a)
    f_b = func(b)
    
    for _ in range(max_iter):
        c = (a + b) / 2
        f_c = func(c)
        
        if abs(f_c) < tol or (b - a) / 2 < tol:
            return c
        
        if f_a * f_c < 0:
            b = c
            f_b = f_c
        else:
            a = c
            f_a = f_c
    
    return (a + b) / 2


def find_x_for_y(x_nodes, y_nodes, target_y):

    def equation(x):
        return lagrange_interpolation(x_nodes, y_nodes, x) - target_y
    
    root = bisection_method(equation, x_nodes[0], x_nodes[-1])
    return root


x_solution = find_x_for_y(x_nodes, y_nodes, y_res)
check_value = lagrange_interpolation(x_nodes, y_nodes, x_solution)


print(f"f(x) = {y_res}")
print(f"Найденное значение x: {x_solution:.10f}")
print(f"Проверка: P({x_solution:.6f}) = {check_value:.10f}")

