import numpy as np

def cobb_dougles(A,K,L):
    return A * (K**0.3) * (L**0.7)

AA = np.arange(1, 10.1, 0.1)
KK = np.arange(1, 10.1, 0.1)
LL = np.arange(1, 10.1, 0.1)
for A in AA:
    for K in KK:
        for L in LL:
            f = cobb_dougles(A,K,L)
            print(f)


