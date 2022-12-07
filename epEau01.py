# exo 1


# our presets 

numbers = ''
newList = []

for i in range(100):

    number = f'{i:02}' # defined the width
    numbers = number # put every numbers in a char
    newList.append(numbers) # put numbers in a list 

# FUNCTION 

def combiOfTwo(var):

    for j in var:
        for k in var[1:]:
            print(f'{j} {k}, ', end='')
    


combiOfTwo(newList)