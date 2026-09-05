def decode(text, step):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    if 1 <= step <= 26:
        res = []
        for i in text:
            if i.isalpha():
                index = alp.index(i.lower())
                ch = alp[(index + step) % 26]
                res.append(ch.upper()) if i.isupper() else res.append(ch)
            else:
                res.append(i)
        return ''.join(res)
    else:
        return


def decode(text, step):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    if 1 <= step <= 26:
        res = []
        for i in text:
            if i.isalpha():
                index = alp.index(i.lower())
                ch = alp[(index - step) % 26]
                res.append(ch.upper()) if i.isupper() else res.append(ch)
            else:
                res.append(i)
        return ''.join(res)
    else:
        return
