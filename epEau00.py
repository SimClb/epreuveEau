import OurLib
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

    for i in myList:
        if OurLib.duplicatorScanner(i):
            blacklist.append(i) # if is True put the combination in the blacklist
        
    for j in blacklist:
        myList.remove(j) # remove the truth combination of the main list (NewList)


    print(myList)
        
########################################################################

inspector(newList)

# ne peut y avoir la chaine inverse (789 est prems donc l'inverse = 987 et ne peut pas être afficher)
# ne peut y avoir deux fois le mm number dans la chaine
#

