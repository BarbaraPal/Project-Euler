# Power digit sum

def vsota_stevk(n):
    stevilo_stevk = len(str(n))
    vsota = 0
    for i in range(stevilo_stevk):
        vsota += int(str(n)[i])
    return vsota

print(vsota_stevk(2**1000))