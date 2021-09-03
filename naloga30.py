# Digit fifth powers

def najdi():
    sez = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for n in range(10):
                            for p in range(10):
                                if i ** 5 + j ** 5 + k ** 5 + l ** 5 + m ** 5 + n ** 5 + p ** 5 == int(str(i) + str(j) + str(k) + str(l) + str(m) + str(n) + str(p)):
                                    sez.append(int(str(i) + str(j) + str(k) + str(l) + str(m) + str(n) + str(p)))
    return sum(sez) - 2  # 0 in 1 ne štejemo zraven

print(najdi())

