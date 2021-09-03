# Number spiral diagonals

def vsota_spiral():
    vsota = 1
    dejanska = 1
    for i in range(2, 1001, 2):
        vsota += i
        dejanska += vsota
        vsota += i
        dejanska += vsota
        vsota += i
        dejanska += vsota
        vsota += i
        dejanska += vsota

    return dejanska    

print(vsota_spiral())
