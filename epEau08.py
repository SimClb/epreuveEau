# Chiffres only 
import sys
import OurLib


# function 

def integerDetector(myChars):

    counter = 0
    for ch in myChars:
        # check if the char is a number
        isNumber = OurLib.isNumericHomeMade(ch)
        if isNumber == True:
            counter += 1
    
    # check if the number of int is the same as the number of chars 
    if counter == OurLib.lenCounter(myChars):
        print('true')
    else:
        print('false')
            


# error management

if OurLib.lenCounter(sys.argv) <= 1:
    print('error.')
    exit()
elif OurLib.lenCounter(sys.argv) > 2:
    print('error.')
    exit()


integerDetector(sys.argv[1])

########################################################################

#finished