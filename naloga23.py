# Non-abundant sums

def faktor(i):
    f = set()
    j = 1
    while not j in f and j < i:
        if i%j == 0:
            f.add(j)
            f.add(i / j)
        j += 1
    return f

def razvrsti(i):
    vsota = sum(faktor(i)) - i
    if vsota < i:
        return -1
    if vsota == i:
        return 0
    if vsota > i:
        return 1

def abundant(i, table):
    a = 0
    b = i
    while a <= b:
        if table[a] == 1 and table[b] == 1:
            return 1
        a += 1
        b -= 1
    return 0

def resi():
    table = []
    for i in range(28124):
        table.append(razvrsti(i))

    s = 0
    for i in range(28124):
        if not abundant(i, table):
            s += i
    return s
print(resi())
