def formatter(*args, value = 'Field', **kwargs):
    res = []
    for i in range(len(args)):
        res.append(f'{value}_{i + 1}: {{{i}}}')

    for key in kwargs:
        res.append(f'{key}: {{{key}}}')

    return '\n'.join(res)


