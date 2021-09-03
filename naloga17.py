# Number letter counts

s1=(0,3,3,5,4,4,3,5,5,4)    # 1 do 9
s11=(0,6,6,8,8,7,7,9,8,8)   # 11 do 19
s10=(0,3,6,6,5,5,5,7,6,6)   # 10 do 90
s=(7,10,11)                 # hundred, hundred and, one thousand

x1 = (sum(s1)*9 + s10[1] + sum(s11) + sum(s10[2:])*10)*10       # od 1 do 99 (10krat)
x2 = s[0]*9 + s[1]*99*9 + sum(s1)*100                           # od 100 do 900
    
vse = x1 + x2 + s[2]

print(vse)