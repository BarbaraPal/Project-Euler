# Even Fibonacci numbers
def fibonacci(stevilo):
    vsota = 0
    prvost = 1
    drugost = 2
    while prvost < stevilo:
        if prvost % 2 == 0:
            vsota += prvost
        prvost, drugost = drugost, prvost + drugost
    return vsota

print(fibonacci(4000000))