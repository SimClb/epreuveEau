#let's recreate basics functions ;) 

def lenCounter(myVar):
    count = 0
    for i in myVar:
        count += 1
    return count


def isNumericHomeMade(myVar):
    try:
        int(myVar)
        isNumeric = True
        return isNumeric
    except ValueError:
        isNumeric = False
        return isNumeric

def exponent(number, exponent):
    result = 1
    for i in range(exponent):
        result *= number
    print(f'the result is: {result}')

def maxHomeMade(myList): 
    #counter of elements of list 
    numberOfElement = 0
    for x in myList:
        numberOfElement += 1   
    
    score = 0
    # take one number and compare to the other
    for i in myList:
        for m in myList[1:]:
            if i > m:            
                score += 1
            else:
                continue

            if score == (numberOfElement - 1):
                print(i)

def minHomeMade(myList):
    #counter of elements of list 
    numberOfElement = 0
    for x in myList:
        numberOfElement += 1   
    
    score = 0
    # take one number and compare to the other
    for i in myList:
        for m in myList[1:]:
            if i < m:            
                score += 1
            else:
                continue

            if score == (numberOfElement - 1):
                print(i)


def double(myList):
    memory = 0
    for i in myList:
        for m in myList:
            if i == m:
                memory = m

    myList.remove(memory)
    print(myList, memory)




