a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


new_list = []

for item in a:
    if item % 2 == 0:
        new_list.append(item)

print(new_list)


#this can be written in less than 2 lines


b = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list2 = [item for item in a if item % 2 == 0]

print(list2)

#EZ