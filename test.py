my_list = [1, 5, 3, 6]

item = 5
secondItem = 3

my_list.remove(item)

print(my_list.index(secondItem) + 1)
my_list.insert((my_list.index(secondItem) + 1), item)

print(my_list)  # 👉️ ['bobby', 'com', 'hadz', '.']
