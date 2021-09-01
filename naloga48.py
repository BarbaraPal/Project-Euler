# Self powers
def vsota(n):
    vsota = 0
    for i in range(1, n + 1):
        vsota += i ** i
    return vsota % (10**10)

print(vsota(1000))
