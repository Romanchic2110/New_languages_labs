def rhombus(h = 5, fill_value = '!'):
    if h % 2 == 0 or h < 1 or h > 49: return
    if len(fill_value) != 1: return
    mid = h // 2
    for i in range(mid + 1):
        stars = 2 * i + 1
        fill = (h - stars) // 2
        print(fill_value * fill + '*' * stars + fill_value * fill)

    for i in range(mid - 1, -1, -1):
        stars = 2 * i + 1
        fill = (h - stars) // 2
        print(fill_value * fill + '*' * stars + fill_value * fill)