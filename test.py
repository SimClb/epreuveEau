import OurLib


newList = ['012', '013', '014', '021']
blacklist = []


for m in newList:

    number = '0'
    number += m[2]
    number += m[1]

    for i in newList:
        if number == i and newList.index(m) < newList.index(i):
            blacklist.append(i)


for m in blacklist:
    newList.remove(m)


print(newList)