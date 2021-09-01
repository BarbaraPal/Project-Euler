# 1000-digit Fibonacci number

def fibonacci_zaporedje(n):
    sez = [1, 1]
    while len(str(sez[-1])) < n:
        sez.append(sez[-1] + sez[-2])
    return len(sez)

print(fibonacci_zaporedje(1000))

