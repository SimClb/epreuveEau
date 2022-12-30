import sys 
import OurLib
import colors


# functions 

def asciiSorter(list):

    notDouble = []

    #create a new list without the double 
    for i in list:
        if not i in notDouble:
            notDouble.append(i)
        
    # we use the bublesort algo
    while not OurLib.isSorterASCII(notDouble): 

        for (i, j) in zip(notDouble, notDouble[1:]):

            if ord(i[0]) > ord(j[0]):
                notDouble.remove(i)
                notDouble.insert((notDouble.index(j) + 1), i)

            elif ord(i[0]) == ord(j[0]):
                if ord(i[1]) > ord(j[1]):
                    notDouble.remove(i)
                    notDouble.insert((notDouble.index(j) + 1), i)

            elif ord(i[0]) < ord(j[0]):
                continue

    for i in notDouble:
        print(i, end=' ')
# error management

if OurLib.lenCounter(sys.argv) <= 1:
    print('error.')
    exit()

# exe 

asciiSorter(sys.argv[1:])


#finished 