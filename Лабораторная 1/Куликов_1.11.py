from random import choices, shuffle

def generate_password(length, /, *, upper, lower, numeric):
    if upper + lower + numeric > length:
        return

    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'

    res = []
    res.extend(choices(up, k = upper))
    res.extend(choices(low, k = lower))
    res.extend(choices(num, k = numeric))

    l = length - len(res)
    if l > 0:
        res.extend(choices(up + low + num, k = l))

    shuffle(res)
    return ''.join(res)
