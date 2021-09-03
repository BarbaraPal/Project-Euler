# Largest palindrome product

def prezrcali(niz):
    return niz[::-1]

def je_palindrom(s):
    return (s == prezrcali(s))

def najdi():
    sez = []
    for i in range(100, 1000):
        for j in range(i, 1000):
            if je_palindrom(str(i * j)):
                sez += [i * j]
    return max(sez)
    
print(najdi())