import OurLib
#combination of 3 numbers 


# function 
#let's generate a list of numbers with 3 numbers 


# our preset of lists 
numbers = ''
newList = []

for i in range(0, 1000):

    number = f'{i:03}' # defined the width
    numbers = number # put every numbers in a char
    newList.append(numbers) # put numbers in a list 


def inspector(myList):

    ourIndex = 0

    #for i in myList:
#
    #    if OurLib.duplicatorScanner(i) == True:
#
    #        del myList[ourIndex]
    #        print(f'the number {i} with index {ourIndex} has been deleted from the list')
    #    
    #    ourIndex += 1
#
    #print(myList)   
        
########################################################################

inspector(newList)

# ne peut y avoir la chaine inverse (789 est prems donc l'inverse = 987 et ne peut pas être afficher)
# ne peut y avoir deux fois le mm number dans la chaine
#

