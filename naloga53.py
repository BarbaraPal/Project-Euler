# Combinatoric selections
def binomski(n, k):
    if k == 0:
        return 1
    else:
        return (n - k + 1) * binomski(n, k - 1) // k

def koliko(n):
    stevilo = 0
    for i in range(1, n + 1):
        for j in range(1,i):
            if binomski(i,j) > 1000000:
                stevilo += 1
    return stevilo

print(koliko(100))
