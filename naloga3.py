# Largest prime factor
def najvecje_prastevilo_ki_deli_stevilo(stevilo, deljitelj):
    while stevilo != 1:
        if stevilo % deljitelj == 0:
            stevilo/=deljitelj
        else:
            deljitelj+=1
    return deljitelj

print(najvecje_prastevilo_ki_deli_stevilo(600851475143, 2))