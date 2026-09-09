def print_receipt(date, discount, products):
    year, month, day = date.split('-')
    keys = list(products.keys())
    values = list(products.values())
    s = 0

    print(f'''=======КАССОВЫЙ ЧЕК=======\n
Дата покупки: {day}.{month}.{year}\n''')

    for i in range(len(products)):
        cost = values[i][0] * values[i][1]
        new_cost = cost / 100 * discount
        s += cost - new_cost
        print(f'{i + 1}. {keys[i]} {values[i][1]} * {values[i][0]} = {cost}')
        print(f'Стоимость со скидкой: {cost - new_cost}\n')

    print(f'''СКИДКА: {discount}%\n\n==========================\n
СУММА ПО ЧЕКУ: {s}''')

print_receipt(date = '2025-02-03', discount = 5, products = {'молоко': (1, 100.0), 'сок': (2, 120.9)})


    