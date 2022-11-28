import time 
import sys

for i in range(len(sys.argv[1])):

    if i % 2 == 0:
        sys.argv[1][i].upper()


var1 = sys.argv[1]
var2 = ""

for i in range(len(var1)):
    if i % 2 == 0:
        var2 += var1[i].upper()
        
    else:
        var2 += var1[i]


print(var2)







