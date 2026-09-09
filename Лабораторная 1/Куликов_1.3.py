def relate_and_translate(alphabet, text):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = alphabet.lower()

    res = []
    for char in text:
        if char.isalpha():
            if char.islower():
                index = alp.index(char)
                res.append(alphabet[index])
            else:
                index = alp.index(char.lower())
                res.append(alphabet[index].upper())
        else:
            res.append(char)

    return ''.join(res)