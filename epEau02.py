#parameters reversed 
import sys 

#function 

def reverser(list1):
    count = 0
    for i in list1:
        count += 1
    
    lastIndex = count - 1 

    for i in range(count - 1):
        print(sys.argv[lastIndex])
        lastIndex -= 1

#secure 

if len(sys.argv) <= 2:
    print("No enough arguments...")
    exit()



reverser(sys.argv)

#finished 
