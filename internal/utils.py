from datetime import datetime

def get_default_date():
    """
    Функция возвращает текущий год и месяц в численном формате по отдельности

    Реализовал format_month - 1 для корректного формирования ссылки т.к. обои
    на текущий месяц выгладываются на месяц раньше.
    """
    format_month = int(datetime.now().strftime('%m'))

    if format_month > 1:
        return datetime.now().strftime('%Y'), '0' + str(format_month - 1)
    else:
        return datetime.now().strftime('%Y'), 12,

def convert_date(year, month):
    """
    Функция возвращает год и месяц в численном формате по отдельности

    Реализовал month - 1 для корректного формирования ссылки т.к. обои
    на текущий месяц выгладываются на месяц раньше.
    """
    month = int(month)
    if month > 1:
        return year, '0' + str(month - 1)
    else:
        return int(year) - 1, 12


def get_month(i):
    """
    Функция имеет словарь, где ключом служат численные представления месяца 
    для их строкового представления.
    """

    d = {
        1: 'january', 
        2: 'february',
        3: 'march',
        4: 'april',
        5: 'may',
        6: 'june',
        7: 'july',
        8: 'august',
        9: 'september',
        10: 'october',
        11: 'november',
        12: 'december',
    }

    return d[i]