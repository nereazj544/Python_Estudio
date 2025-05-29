import datetime


def edad (age_year):
    hoy : int = datetime.date.today()
    return hoy.year - age_year


mi_edad = edad(2004)
hoy : int = datetime.date.today()
print(f"Este año {hoy.year} mi edad sera: {mi_edad} años")