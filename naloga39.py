# Integer right triangles

def vsote():
    sez = []
    for a in range(1, 400):
        for b in range(1, 400):
            for c in range(1, 400):
                if a ** 2 + b ** 2 == c ** 2:
                    obseg = a + b + c
                    sez.append(obseg)
    sez.sort()
    return sez
    
print(vsote())
