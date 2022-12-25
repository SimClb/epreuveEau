import OurLib

my_list = [6, 8, 5, 1, 3, 2, 4]

m = int(my_list[0])

for i in my_list[1:]:

    if int(i) < m: 
        m = int(i)

print(m)


print(OurLib.isSorter(my_list))