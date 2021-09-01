# Powerful digit sum

def vsota_stevk(n):
    stevilo_stevk = len(str(n))
    vsota = 0
    for i in range(stevilo_stevk):
        vsota += int(str(n)[i])
    return vsota
    
def najvecja_vsota(n):
    vsota = 0
    for i in range(1, n):
        for j in range(1, n):
            vsota = max(vsota, vsota_stevk(i ** j))
    return vsota

print(najvecja_vsota(100))
