"""
Tengo 50€ para comrar una camisa, si la camisa cuesta 35€ y tiene un descuento del 10%,
¿cuanto dinero tender despues de comprar la camisa?

"""

# DATOS
dinero = 50
camisa = 35
descuento = 10

# CALCULO 
total_precio_camisa = camisa * (descuento/100)
total_precio_camisa = camisa - total_precio_camisa
dinero_restante = dinero - total_precio_camisa
print(f"El precio de la camisa con descuento es: {total_precio_camisa:.2f}€")
print(f"El dinero que me queda después de comprar la camisa es: {dinero_restante:.2f}€")