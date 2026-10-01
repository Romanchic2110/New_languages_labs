x_nodes = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
y_nodes = [0.946083, 1.028685, 1.108047, 1.183958, 1.256227,
           1.324684, 1.389181, 1.449592, 1.505817, 1.557775]


t_points = [0.129140, 0.766507, 0.238812]


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


def select_nodes(x_nodes, y_nodes, t, k=4):
    
    pairs = [(abs(x - t), i) for i, x in enumerate(x_nodes)]
    pairs.sort()
    
    idx = sorted(i for _, i in pairs[:k])
    
    xs = [x_nodes[i] for i in idx]
    ys = [y_nodes[i] for i in idx]
    return xs, ys


print(f"Точки интерполяции: t1 = {t_points[0]}, t2 = {t_points[1]}, t3 = {t_points[2]}")

for i, t in enumerate(t_points, 1):
    xs, ys = select_nodes(x_nodes, y_nodes, t, k=4)
    
    lag_val = lagrange_interpolation(xs, ys, t)
    new_val = newton_interpolation(xs, ys, t)
    
    print(f"\nТочка t{i} = {t}")
    print(f"  Использованные узлы: {xs}")
    print(f"  Значение по Лагранжу: {lag_val:.6f}")
    print(f"  Значение по Ньютону:  {new_val:.6f}")

