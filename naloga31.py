# Coin sums

def koliko():
    nacini = [0]*201
    nacini[0] = 1
    for x in [1,2,5,10,20,50,100,200]:
        for i in range(x, 201):
            nacini[i] += nacini[i-x]
    return nacini[200]

print(koliko())