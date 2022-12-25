# tri par sélection 
import sys
import OurLib
import colors

# function 

def selectionSort(mylist):
    

    # let's work in a list without doubles

    notDouble = [] 

    for i in mylist:

        if not i in notDouble:
            notDouble.append(int(i))

    # put a while loop to stop when is sorted 

    # our presets: 

        i = 0 

    while not OurLib.isSorter(notDouble):

        # let's find the min 
        m = notDouble[i]
        for j in notDouble[i:]:

            if j < m:
                m = j

        # let's check if the min is not already at the good place if no put it at the good place
        if i != notDouble.index(m):
            notDouble.remove(m)
            notDouble.insert(i, m)

        i += 1


    for i in notDouble:
        print(i, end=' ')

# error management 

if OurLib.lenCounter(sys.argv) < 4:
    print('error.')
    exit()

for i in sys.argv[1:]:
    if not OurLib.isNumericHomeMade(i):
        print('error.')
        exit()

# exe 

selectionSort(sys.argv[1:])

# finished



