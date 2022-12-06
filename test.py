import colors


def duplicatorScanner(var):

    counterI = 0
    counterJ = 0

    for i in var:
        print(colors.bcolors.OKBLUE, counterI, "qui est l'index de:", i, colors.bcolors.ENDC)

        for j in var:
            print(colors.bcolors.OKGREEN, counterJ, "qui est l'index de:", j,  colors.bcolors.ENDC)
            if i == j and counterI != counterJ:
                print(f'{i} ayant pour index {counterI} est égal à {j} ayant pour index {counterJ}')
                return True
                

            counterJ += 1

        counterI += 1
        counterJ = 0
            

number = ['001', '107', '003']

for g in number:
    print(g)
    if duplicatorScanner(g):
        print('ok')
        number.remove(g)
    else:
        print('pas ok')

print(number)