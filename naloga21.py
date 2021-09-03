
def delitelji(stevilo):
    sez = []
    for i in range(1, stevilo):
        if stevilo % i == 0:
            sez.append(i)
    return sez

def vsota_deljiteljev(stevilo):
    return sum(delitelji(stevilo))

def ali_je_prijateljsko_stevilo(stevilo):
    vsota = vsota_deljiteljev(stevilo)
    if vsota_deljiteljev(vsota) == stevilo and vsota_deljiteljev(stevilo) == vsota and vsota != stevilo:
        return True
    else:
        return False
    
def celotna_vsota():
    vsota = 0
    for k in range(10000):
        if ali_je_prijateljsko_stevilo(k):
            vsota += k
    return vsota

print(celotna_vsota())