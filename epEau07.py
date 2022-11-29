### Majuscule ###
import sys
import OurLib
import re


# functions

def spliter(myChars):

    #split by space my words
    words = myChars.split(' ')
    output = ""

    # for each word replace the first letter with a maj
    for word in words:
        word = word[0].upper() + word[1:]
        output += word + ' '

    print(output)


# error management 

if OurLib.lenCounter(sys.argv) <= 1:
    print('error.')
    exit()
elif OurLib.lenCounter(sys.argv) > 2:
    print('error.')
    exit()

isNumber = OurLib.isNumericHomeMade(sys.argv[1])

if isNumber == True:
    print('error.')
    exit()
else:
    spliter(sys.argv[1])

########################################################################

#finished