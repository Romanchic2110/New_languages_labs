from collections import defaultdict

def most_common_error(func, args):
    results = []              
    errors_by_type = defaultdict(list)
    popular_groups = []
    
    for arg in args:
        try:
            results.append(func(*arg))
        except Exception as e:
            errors_by_type[type(e)].append(e)
    
    if not errors_by_type:
        return results
    

    max_count = max(len(errs) for errs in errors_by_type.values())
    

    for exc_type, exc_list in errors_by_type.items():
        if len(exc_list) == max_count:
            group = ExceptionGroup(f'Группа ошибок типа {exc_type.__name__}', exc_list)
            popular_groups.append(group)
    
    
    raise ExceptionGroup(f'Группа наиболее распространенных ошибок при вызове функции {func.__name__}()', popular_groups)
