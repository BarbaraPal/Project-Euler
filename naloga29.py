# Distinct powers

def koliko_potenc():
    sez = []
    for a in range(2, 101):
        for b in range(2, 101):
            sez.append(a ** b)
    return sez

def izloci_iste(sez):
    podvojeni = 0
    for i in range(len(sez)):
        if sez[i] in sez[:i] :
            podvojeni += 1
    return len(sez) - podvojeni
        

print(izloci_iste(koliko_potenc()))