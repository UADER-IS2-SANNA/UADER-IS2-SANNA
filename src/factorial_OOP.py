#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                        *
#* Calcula los factoriales en un rango de números usando POO               *
#* Basado en factorial.py                                                   *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    def __init__(self, min_val=1, max_val=60):
        self.min_val = min_val
        self.max_val = max_val
    
    def calcular_factorial(self, num):
        if num < 0:
            print(f"Factorial de {num} no existe")
            return None
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact
    
    def run(self, min_num, max_num):
        if min_num > max_num:
            print("Error: el primer número debe ser menor o igual al segundo.")
            return
        for num in range(min_num, max_num + 1):
            print(f"Factorial {num}! es {self.calcular_factorial(num)}")

# Manejo de entrada
if len(sys.argv) == 1:
    entrada = input("Ingrese un número o un rango (ej. 4-8, -10, 5-): ")
else:
    entrada = sys.argv[1]

# Procesamiento de la entrada
try:
    if "-" in entrada:
        if entrada.startswith("-"):
            hasta = int(entrada[1:])
            desde = 1
        elif entrada.endswith("-"):
            desde = int(entrada[:-1])
            hasta = 60
        else:
            desde, hasta = map(int, entrada.split("-"))
        
        factorial_obj = Factorial()
        factorial_obj.run(desde, hasta)
    else:
        num = int(entrada)
        factorial_obj = Factorial()
        print(f"Factorial {num}! es {factorial_obj.calcular_factorial(num)}")
except ValueError:
    print("Error: entrada no válida. Use desde-hasta, -hasta o desde-.")
