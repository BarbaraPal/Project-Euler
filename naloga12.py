def trikotniska_stevila(n):
    vsota = 0
    for i in range(1, n + 1):
        vsota += i
    return vsota

def najdi():
    j = 0
    n = 0
    st_deliteljev = 0
    while st_deliteljev <= 500:
        st_deliteljev = 0
        j += 1
        n = trikotniska_stevila(j)
        i = 1
        while i <= n ** 0.5:
            if n % i == 0:
                st_deliteljev += 1
            i += 1
    st_deliteljev *= 2
    return n

print(najdi())