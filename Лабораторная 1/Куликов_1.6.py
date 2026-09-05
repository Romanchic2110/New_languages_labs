def convert_digits(num):
    for i in str(num):
        n = int(i)
        if n == 0:
            print(str(n).center(999, '*'))
        elif n % 2 == 0:
            print(str(n).rjust(n, '+'))
        else:
            print(str(n).ljust(n, '-'))

