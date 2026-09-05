def relate_and_translate(alphabet, text):
    alp = 'absdefghigklmnopqrstuvwxyz'
    alphabet = alphabet.lower()
    res = []
    for i in text.lower():
        index = alp.index(i)
        res.append(alphabet[index])
    return ''.join(res)
