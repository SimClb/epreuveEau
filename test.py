import time 
import sys

isPrime = False
ourNumber = int(sys.argv[1])
count = 0

while isPrime == False:

    for i in range(1,11):
        if int(sys.argv[1]) % i == 0:
            count += 1
        else: 
            continue
        
        
    if count == 2:
        print("It's a prime number")
        isPrime = True
        exit()
    elif count != 2:
        ourNumber += 1
        isPrime = False
    
