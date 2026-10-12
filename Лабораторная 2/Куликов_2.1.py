def evaluate(func, *args):
    try:
        return func(*args)
    except Exception:
        return 'Во время выполнения произошла ошибка'
