import math

class NegativeResultError(Exception):
    pass

def convert(data):
    conversion_errors = []
    arithmetic_errors = []  
    results = []
    groups = []

    for s in data:
        try:
            number = int(s)
        except ValueError as e:
            e.add_note(f"Ошибка обработки строки '{s}'")
            conversion_errors.append(e)
            continue
        

        try:
            result = math.sqrt(100 / number)
            results.append(result)
        except ZeroDivisionError as e:
            e.add_note(f"Ошибка обработки строки '{s}'")
            arithmetic_errors.append(e)
        except ValueError:
            err = NegativeResultError(f'Нельзя извлечь корень из отрицательного числа {100 / number}')
            err.add_note(f"Ошибка обработки строки '{s}'")
            arithmetic_errors.append(err)
    

    if conversion_errors:
        groups.append(ExceptionGroup('Ошибки преобразования', conversion_errors))
    if arithmetic_errors:
        groups.append(ExceptionGroup('Ошибки арифметических операций', arithmetic_errors))
    if groups:
        raise ExceptionGroup('Во время обработки строк произошло несколько ошибок', groups)
    
    return results