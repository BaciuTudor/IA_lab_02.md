import numpy as np

np.random.seed(21)
A = np.random.randint(1, 10, size=(4, 3))
B = np.random.randint(1, 10, size=(3, 5))

print("Matricea A:")
print(A)

print("\nMatricea B:")
print(B)

C = A @ B
print("\nMatricea C = A @ B:")
print(C)

print("\nSuma tuturor elementelor din C:")
print(np.sum(C))

print("\nMedia pe fiecare coloană (axis=0):")
print(np.mean(C, axis=0))

print("\nValoarea maximă globală:")
print(np.max(C))

M = np.random.randint(1, 10, size=(3, 3))
print("Matricea M:")
print(M)

M_inv = np.linalg.inv(M)
print("\nInversa lui M:")
print(np.linalg.inv(M))

det_M = np.linalg.det(M)
print(f"\nDeterminantul lui M: {det_M}")

product = M @ M_inv
identity = np.eye(3)
print("\nM @ M_inv:")
print(product)

print("\nMatricea identitate:")
print(identity)

is_identity = np.allclose(product, identity)
print(f"\nM @ M_inv este aproape de matricea identitate: {is_identity}")