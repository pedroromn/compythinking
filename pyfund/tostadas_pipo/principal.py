from utilidades import impuestos
from utilidades import calculos


monto = int(input("Introduzca un monto entero: "))
# Llama la función definida en el módulo "impuestos"
print(f"El impuesto IVA de 12%: {impuestos.impuesto_iva12(monto)}")

suma = int(input("Introduzca un monto entero a sumar: "))
print(f"La suma total es: {calculos.suma_total(suma)}")
