import OurLib
import colors
#combination of 3 numbers 


# function 
#let's generate a list of numbers with 3 numbers 


# our preset of lists 
numbers = ''
newList = []

for i in range(12, 790):

    number = f'{i:03}' # defined the width
    numbers = number # put every numbers in a char
    newList.append(numbers) # put numbers in a list 


def inspector(myList):

    blacklist = []


    ####################### del the duplicators ###########################

    for i in myList:
        if OurLib.duplicatorScanner(i):
            blacklist.append(i) # if is True put the combination in the blacklist
        
    for j in blacklist:
        myList.remove(j) # remove the truth combination of the main list (NewList)

    ####################### del the 100 first reverses ############################

    blacklist.clear()  # let's clear our blacklist to use it again 

    for n in myList:

        if int(n) < 100:

            number = '0'
            number += n[2]
            number += n[1]

            for o in myList:
                
                if number == o and myList.index(n) < myList.index(o):

                    blacklist.append(o)


    ####################### del all reverses ############################

    for k in myList:
        for l in myList:
            
            if OurLib.reverseStr(k) == l and myList.index(k) < myList.index(l):
                blacklist.append(l)
            
    for m in blacklist:
        myList.remove(m)

    # LETS PRINT THE RESULT 

    for k in myList:
        print(f'{k}, ', end="")
        
########################################################################

inspector(newList)

#finished

