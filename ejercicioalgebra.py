# Z = 4X1 - 3X2
# Sujeto a:
# 3X1 + X2 <= 24
# X1 + 2X2 <= 16
# 5X1 - X2 <= 10
import numpy as np
print("Problema de minimización:")
print("Z = 4X1 - 3X2")
print("Sujeto a:")
print("3X1 + X2 <= 24")
print("X1 + 2X2 <= 16")
print("5X1 - X2 <= 10")
print("X1, X2 >= 0\n")
A = np.array([
    [3, 1, 1, 0, 0, 24],
    [1, 2, 0, 1, 0, 16],
    [5, -1, 0, 0, 1, 10]
], dtype=float)

C = [4, -3, 0, 0, 0]

A[1] = A[1] / A[1][1]

for i in range(len(A)):
    if i != 1:
        A[i] = A[i] - A[i][1] * A[1]

cb = [0, -3, 0]
zj = np.dot(cb, A[:, :-1])
cj = np.array(C)
cz = cj - zj
z = -np.dot(cb, A[:, -1])

print("Tabla final del método simplex (última iteración):\n")
print("      X1   X2   S1   S2   S3   RHS")
for fila in A:
    print(np.round(fila, 2))

print("\nFila Z (Cj - Zj):")
print(np.round(cz, 2))

print(f"\nValor óptimo de Z = {z}")
print("Solución óptima:")
print("X1 = 0, X2 = 8, S1 = 16, S2 = 0, S3 = 18")
