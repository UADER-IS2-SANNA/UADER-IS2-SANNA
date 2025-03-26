#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* Calcula los factoriales en un rango de números                          *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return None
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

# Verifica si se pasó un argumento, si no, lo solicita manualmente
if len(sys.argv) == 1:
    entrada = input("Ingrese un número o un rango (ej. 4-8): ")
else:
    entrada = sys.argv[1]

# Manejo del rango desde-hasta
if "-" in entrada:
    try:
        desde, hasta = map(int, entrada.split("-"))
        if desde > hasta:
            print("Error: el primer número debe ser menor o igual al segundo.")
        else:
            for num in range(desde, hasta + 1):
                print(f"Factorial {num}! es {factorial(num)}")
    except ValueError:
        print("Error: formato de entrada incorrecto. Use desde-hasta, ej. 4-8.")
else:
    try:
        num = int(entrada)
        print(f"Factorial {num}! es {factorial(num)}")
    except ValueError:
        print("Error: entrada no válida.")







