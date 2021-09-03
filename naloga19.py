# Counting Sundays

neprestopno_leto = [31,28,31,30,31,30,31,31,30,31,30,31]
prestopno_leto = [31,29,31,30,31,30,31,31,30,31,30,31]

leto = [ neprestopno_leto ] * 100
for i in range(3, len(leto), 4) :
    leto[i] = prestopno_leto

trenutno = 365 % 7
nedelje = 0
for i in leto :
    for j in i :
        if trenutno % 7 == 6:
            nedelje += 1
        trenutno += j % 7
print (nedelje)

