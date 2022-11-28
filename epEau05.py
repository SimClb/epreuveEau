# string in string 
import OurLib
import sys


# function 

def finder(ourBase, string):
    if string in ourBase:
        print('true')
    else:
        print('false')



# security 

if OurLib.lenCounter(sys.argv) <= 1:
    print('Error number of arguments')
    exit()
elif OurLib.lenCounter(sys.argv) > 3:
    print('Error number of arguments')
    exit()

for i in sys.argv: 
    try: 
        int(i)
    except ValueError:
        continue
    if int(i):
        print("error.")
        exit()

################################################################

finder(sys.argv[1], sys.argv[2])


#finished 