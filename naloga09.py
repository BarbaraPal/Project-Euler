#Special Pythagorean triplet

def pitagora(n):
    for i in range(1, n):
        for j in range(1, n):
            a = i
            b = j
            c = n - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a*b*c
    return 'Ta pitagorejska trojica ne obstaja!'


print(pitagora(1000))