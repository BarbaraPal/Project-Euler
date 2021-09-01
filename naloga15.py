# Lattice paths

def binomski(n, k):
    if k == 0:
        return 1
    else:
        return (n - k + 1) * binomski(n, k - 1) // k

print(binomski(40, 20))
