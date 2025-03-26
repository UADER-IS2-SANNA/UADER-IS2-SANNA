#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* collatz.py                                                              *
#* Calcula la cantidad de iteraciones necesarias para llegar a 1 en la    *
#* secuencia de Collatz para los números del 1 al 10000 y los grafica.     *
#*-------------------------------------------------------------------------*
import matplotlib.pyplot as plt

def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

# Generar datos
numbers = list(range(1, 10001))
iterations = [collatz_steps(n) for n in numbers]

# Graficar
plt.figure(figsize=(10, 5))
plt.scatter(numbers, iterations, s=1, color='blue')
plt.xlabel("Número inicial (n)")
plt.ylabel("Número de iteraciones")
plt.title("Número de iteraciones en la secuencia de Collatz")
plt.grid(True)
plt.show()
