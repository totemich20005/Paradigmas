# Ejemplo de Programación Imperativa
# Programa que calcula el promedio de varias notas
# y determina si el estudiante aprobó o reprobó.

cantidad_notas = int(input("¿Cuántas notas desea ingresar?: "))

suma_notas = 0

for i in range(cantidad_notas):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    suma_notas = suma_notas + nota

promedio = suma_notas / cantidad_notas

print("El promedio del estudiante es:", promedio)

if promedio >= 3.0:
    print("El estudiante APROBÓ.")
else:
    print("El estudiante REPROBÓ.")