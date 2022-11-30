import sys 
import OurLib
#index wanter

# function

def indexWanted(myArray):

    endIndex = OurLib.lenCounter(myArray) - 1

    indexCounter = 0

    for i in myArray[:endIndex]:

        if i == myArray[endIndex]:
            print(indexCounter)
            exit()
        else:
            indexCounter += 1
            continue

    print(-1)
            

# error management

if OurLib.lenCounter(sys.argv) <= 1:
    print('error')

################################################################

indexWanted(sys.argv[1:])


#finished