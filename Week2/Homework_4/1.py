A = float(input("A"))
K = float(input("K"))
L = float(input("L"))
def cobb_dougles(A,K,L):
    return A * (K**0.3) * (L**0.7)
result = cobb_dougles(A,K,L)
print(result)
