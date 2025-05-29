"""
En enero de este año acutal tenia una cuenta con 3000€. Si cobro 1.100€ mensuales y tengo unos gastos fijos al mes de 435€. 
¿a cuanto asciende mis gastos extra mensuales si al final del año mi cuenta tiene un total de 6000€?
"""

cobra = 1100 * 12
total_dinero = 3000 + cobra
gastos_fijos = 435 * 12
total_dinero_con_gastos = total_dinero - gastos_fijos
gastos_extra = total_dinero_con_gastos - 6000
print(f"Mis gastos extra mensuales son: {gastos_extra / 12:.2f}€")


# OTRA FORMA DE HACERLO
# DATOS 
cuenta = 3000
cobra = 1100 *12
gastos_fijos = 435 * 12
cuenta_final = 6000

# CALCULO 
total_cuenta = cuenta + cobra
print(f"Total de la cuenta al final del año: {total_cuenta}€ (sin gastos)")	
total_cuenta_gastos = total_cuenta - gastos_fijos
print(f"Total de la cuenta al final del año: {total_cuenta_gastos}€ (con gastos fijos)")
total_gastos_extra = total_cuenta_gastos - 6000
print(f"Total de gastos extra al mes: {total_gastos_extra/12:.2f}€")

