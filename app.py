# Simple ist to set prog

# gonna use a function for it

def to_set(list1):
    list1 = set(list1)  # convert to set i.e eradicating duplicates
    list1 = list(list1)  # convert back to list without duplicates
    return list1
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 10, 4, 20, 4, 9]

list2 = to_set(b)

print(list2) # prints without duplicates


def convert_list(list1):
    y = []
    for item in list1:
        if item not in y:
            y.append(item)
            '''So this uses reverse logic
                Y is an empty list that appends the values of list1 
                so if the item does not already exist in Y append it
                cool use of {not in}
            '''