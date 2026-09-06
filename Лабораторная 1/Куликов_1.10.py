def convert_temperature(temp, /, *, scale):
    if scale == 'C':
        temp = temp * 1.8 + 32
        scale = 'F'
    elif scale == 'F':
        temp = (temp - 32) * (5/9)
        scale = 'C'
    return f'{temp:.2f} °{scale}'
