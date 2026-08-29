import calendar

def dias_del_mes(anio, mes):
    return calendar.monthrange(anio, mes)[1]

print(dias_del_mes(2026, 6)) 