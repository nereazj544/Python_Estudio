"""
Mi coche gasta 5,5 litros cada 100 km y mi trabajo se encuentra a 15 km de casa.
¿Cuanto me gastare en gasolina en 20 dias laborales si el precio es de 1,12€/L?
"""

precio = 1.12
km = 15 
litors_100km = 5.5
dias_laborales = 20

# Calculo del gasto de gasolina

gasto = (km * litors_100km / 100) * precio * dias_laborales
print(f"El gasto en gasolina en {dias_laborales} dias laborales es de: {gasto:.2f}€")



