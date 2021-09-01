# Longest Collatz sequence

def naslednji_clen(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def dolzina_zaporedja(n):
    dolzina = 1
    while n != 1:
        n = naslednji_clen(n)
        dolzina += 1
    return dolzina

def najvecji_clen(n):
    najvecji = n
    while n != 1:
        n = naslednji_clen(n)
        najvecji = max(n, najvecji)
    return najvecji

def najdaljse_zaporedje(m, n):
    dolzina = 0
    for k in range(m, n + 1):
        if dolzina_zaporedja(k) > dolzina:
            dolzina = dolzina_zaporedja(k)
            stevilo = k
    return stevilo

print(najdaljse_zaporedje(1, 1000000))