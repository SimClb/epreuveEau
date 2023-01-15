#fibonacci sequence 
import sys
import OurLib

# functions 

# rule: Xn = Xn-1 + Xn-2

def fibSequence(userSet):

    list = [0, 1]

    n=0
    m=1
    #each loop do the rule of fib sequence (Xn = Xn-1 + Xn-2)
    while m < int(userSet): 
        calcul = list[n] + list[m]
        list.append(calcul)
        n += 1
        m += 1

    print('By while loop; ' ,list[m])

def rescFibSeq(idx):

    if int(idx) <= 1:
        return idx
    else:
        return rescFibSeq(int(idx) - 1) + rescFibSeq(int(idx) - 2)
    
# secure 

if OurLib.lenCounter(sys.argv) <= 1:
    print('Error number of arguments')
    exit()
elif OurLib.lenCounter(sys.argv) > 2:
    print('Error number of arguments')
    exit()

if OurLib.isNumericHomeMade(sys.argv[1]) == False:
    exit()
elif int(sys.argv[1]) < 0:
    print('negative number of arguments')
    exit()


fibSequence(sys.argv[1])
print('By recursivity function; ' ,rescFibSeq(sys.argv[1]))


#finished