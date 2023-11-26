my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = []

for x in my_list:
    if x % 2 == 0:
        new_list.append(x)

print(new_list)
