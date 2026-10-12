from datetime import date

class InvalidDateError(Exception):
    pass

def parse_date(date_str):
    try:
        day, month, year = date_str.split('.')
        day, month, year = int(day), int(month), int(year)
        
        if not (1 <= day <= 31 and 1 <= month <= 12):
            raise InvalidDateError('Некорректная дата')
        
        return date(year, month, day)
    
    except (ValueError, AttributeError):
        raise InvalidDateError('Некорректная дата')


