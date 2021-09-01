# Multiples of 3 or 5
def vsota(stevka):
    vsota = 0
    for i in range(1, stevka):
        if i % 3 == 0:
            vsota += i
            continue
        elif i % 5 == 0:
            vsota += i
        else:
            pass
    return vsota

print(vsota(1000))