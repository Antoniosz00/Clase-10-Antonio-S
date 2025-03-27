# Proyecto: Clase 10 del curso Fundamentos de Python
# Estudiante: Antonio Sánchez Zárate 
# Fecha de Inicio: 25 de marzo del 2025
# Fecha de Entrega: 25 de marzo del 2025
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.

from analisis_datos.carga_datos import generar_lista_compras
from analisis_datos.estadisticas import media
lista_compras = generar_lista_compras()

print(lista_compras)


precios = [valor for producto,valor in lista_compras]


print("La media compra:", media(precios))

precios_asc = sorted(precios)
print(precios)

n = len(precios_asc)

mitad = n // 2
if n % 2 == 0:
    mediana = (precios[mitad -1] + precios_asc [mitad])/2
else:
    mediana = precios_asc[mitad]    
print(4 % 2 == 0)
print("La mediana de la compra es:" ,mediana)
