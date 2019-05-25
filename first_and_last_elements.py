
# in a function, get the first and last elements of a list

def get_elements(list):
    new_list = ['']
    # for some reason this only works when the list has an empty element
    # probably needed to be intialized
    new_list[0] = list[0]
    new_list.append(list[-1])
    return new_list




a = [5, 10, 15, 20, 25]

print(get_elements(a))





