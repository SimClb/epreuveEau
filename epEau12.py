import sys
import colors
import OurLib
# BUBBLE SHORT ALGO 

# function 

def isSorter(list):

    members = (OurLib.lenCounter(list) - 1) 
    counter = 0

    for (i, j) in zip(list, list[1:]):

        if i < j:
            counter += 1

    if counter == members:
        return True


def bubbleSort(myList):

    notDouble = []

    for i in myList:
        if i not in notDouble:
            notDouble.append(i) # like that we are working in a simple list !

    while not isSorter(notDouble):

        for (i, j) in zip(notDouble, notDouble[1:]):
            if i > j: 
                notDouble.remove(i)
                notDouble.insert((notDouble.index(j) + 1), i)
            elif i < j:
                continue
                
    for i in notDouble:
        print(i, end=' ')

# error management 

if OurLib.lenCounter(sys.argv) <= 1:
    print('error.')
    exit()

for i in sys.argv[1:]:

    if not OurLib.isNumericHomeMade(i):
        print('error.')
        exit()

################################################################

intList = []

for i in sys.argv[1:]:
    intList.append(int(i))

bubbleSort(intList)

#finished