import time 
import sys

count = 0
count2 = 1

list = [0, 1]

userSet = int(sys.argv[1])

n=0
m=1

while m < userSet: 
    calcul = list[n] + list[m]
    list.append(calcul)
    n += 1
    m += 1


print(list)
    
    
