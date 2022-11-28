# next prime number 
import sys
import OurLib

# function 
# it will try to divide the number by the number from 1 to 10
def primeNumber(fromNumber):
    count =  0
    for i in range(1, 11):
        if int(fromNumber) % i == 0:
            count += 1
        else:
            continue

    if count == 2:
        isPrime = True
        return isPrime
    else:
        isPrime = False
        return isPrime

    

# security 

if OurLib.lenCounter(sys.argv) <= 1:
    print('Error number of arguments')
    exit()
elif OurLib.lenCounter(sys.argv) > 2:
    print('Error number of arguments')
    exit()

try:
    int(sys.argv[1])
except ValueError:
    print("-1")
    exit()

if int(sys.argv[1]) < 0:
    print("-1")
    exit()

################################################################

ourNumber = int(sys.argv[1]) +  1

# loop to check the next prime number
while primeNumber(ourNumber) == False:
    ourNumber += 1
    

print(ourNumber)

#finished 
