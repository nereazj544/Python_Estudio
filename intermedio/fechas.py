# fecha

import datetime

def actual_fecha():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def fecha_ayer():
    return (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

print("Fecha y hora actual:", actual_fecha())

print("Fecha de ayer:", fecha_ayer())
