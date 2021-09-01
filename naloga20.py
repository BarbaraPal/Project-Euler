# Factorial digit sum

def fakulteta(n):
    produkt = 1
    if n == 0: 
        return 1
    else:
        for i in range(1, n+1):
            produkt *= i
    return produkt

def vsota_stevk(n):
    vsota = 0
    st = fakulteta(n)
    st = str(st)
    for i in range(len(st)):
        vsota += int(st[i])
    return vsota

print(vsota_stevk(100))