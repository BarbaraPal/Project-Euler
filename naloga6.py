# Sum square difference
def razlika(n):
    vsota_kvadratov = 0
    vsota = 0
    for i in range(1, n+1):
        vsota += i
    for i in range(1,n+1):
        vsota_kvadratov += i ** 2
    return vsota ** 2 - vsota_kvadratov

print(razlika(100))