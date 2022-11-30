# entre min et max
import sys
import OurLib

# data preparation

list = sys.argv[1:]
secondList = []
for i in list:
    secondList.append(int(i))


# function 

def includedPrinter():

    if secondList[0] < secondList[1]:
        rangeIndex = secondList[1] - secondList[0]
        starting = secondList[0]
    else:
        rangeIndex = secondList[0] - secondList[1]
        starting = secondList[1]

    output = ""

    for m in range(rangeIndex):
        output += f'{starting}' + ' '
        starting += 1

    print(output)
    

# error management 

if OurLib.lenCounter(sys.argv) != 3:
    print('error')
    exit()

for i in sys.argv[1:]:
    isNumber = OurLib.isNumericHomeMade(i)
    if isNumber == False:
        print('error')
        exit()

if secondList[0] == secondList[1] or secondList[0] == secondList[1] - 1 or secondList[0] == secondList[1] + 1:
    print('error')
    exit()

################################################################

includedPrinter()
#finished 

# pseudo code: 

# prendre argv 1 et 2 regarder le plus grand et le plus petit 
# faire sous straction = au nbre de range 
# pour chaque boucle afficher argv min + 1 en omettant 