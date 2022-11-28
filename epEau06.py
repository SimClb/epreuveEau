import sys
import OurLib
#majEver2 Maj deux sur deux


# function 

def majOn(listOfChars):

    newChars = ""
    # take the index by a loop 
    for i in range(OurLib.lenCounter(listOfChars)):
        if i % 2 == 0:
            newChars += listOfChars[i].upper()
        else:
            newChars += listOfChars[i]

    print(newChars)

        


# eror management

listOfArgv = sys.argv

if OurLib.lenCounter(listOfArgv) != 2:
    print('error')
    exit()


for i in listOfArgv:
    try:
        int(i)
        exit()
    except ValueError:
        isNumer = False

################################################################

majOn(sys.argv[1])

#finished